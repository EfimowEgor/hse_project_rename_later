from aiohttp import ClientSession, ClientConnectorError
from api_infrastructure import urls
from api_infrastructure.models import *


async def get_data_from_api(url: str, params=None) -> dict|list[dict]|None:
    if params is not None:
        url = add_params(url, params)
        
    print(url)
    
    try:
        async with ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                print(response.status)
                
    except ClientConnectorError as ex:
        print(ex)
    
    return None


def add_params(url: str, params: dict[str, str]):
    return f'{url}?{"&".join([f"{key}={value}" for key, value in params.items()])}'
    

async def has_student(first_name: str, last_name: str, patronymic: str) -> bool:
    params = {
        'firstName': first_name,
        'lastName': last_name,
        'patronymic': patronymic
    }
    
    return await get_data_from_api(urls.has_student_url, params)


async def get_students_by_one_part_name(part_name: str) -> list[Student]:
    params = {
        'partName': part_name,
    }
    
    students = await get_data_from_api(urls.get_students_by_one_part_name_url, params)
    return map_students(students)


async def get_students_by_two_parts_name(part_name_1: str, part_name_2: str) -> list[Student]:
    params = {
        'partName1': part_name_1,
        'partName2': part_name_2
    }
    
    students = await get_data_from_api(urls.get_students_by_two_parts_name_url, params)
    return map_students(students)


def map_students(students: list[dict]) -> list[Student]:
    return [Student(student['firstName'], student['lastName'], student['patronymic']) for student in students]


async def get_current_student_ratings_by_name(first_name: str, last_name: str, patronymic: str):
    params = {
        'firstName': first_name,
        'lastName': last_name,
        'patronymic': patronymic
    }
    
    ratings = await get_data_from_api(urls.get_current_student_ratings_by_name_url, params)
    return map_student_ratings(ratings)


async def get_after_retake_student_ratings_by_name(first_name: str, last_name: str, patronymic: str):
    params = {
        'firstName': first_name,
        'lastName': last_name,
        'patronymic': patronymic
    }
    
    ratings = await get_data_from_api(urls.get_after_retake_student_ratings_by_name_url, params)
    return map_student_ratings(ratings)


async def get_cumulative_student_ratings_by_name(first_name: str, last_name: str, patronymic: str):
    params = {
        'firstName': first_name,
        'lastName': last_name,
        'patronymic': patronymic
    }
    
    ratings = await get_data_from_api(urls.get_cumulative_student_ratings_by_name_url, params)
    return map_student_ratings(ratings)


def map_student_ratings(student_ratings: list[dict]) -> list[StudentRating]:
    return [StudentRating(student_rating['programName'], 
                    student_rating['course'], 
                    student_rating['years'],
                    student_rating['modules'],
                    student_rating['place'],
                    student_rating['meanGrade'],
                    student_rating['minGrade'],
                    student_rating['percentile'],
                    student_rating['gpa']) for student_rating in student_ratings]
