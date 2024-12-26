from api_infrastructure import api
from bot_infrastructure import messages


async def handle_start_command(message: str) -> tuple[bool, str]:
    return True, messages.welcome_message


async def handle_find_student_by_incomplete_name_command(message: str) -> tuple[bool, str]:
    words = message.split()
    
    if len(words) != 1:
        part_name_1 = words[0]
        part_name_2 = ' '.join(words[1:])
        students = await api.get_students_by_two_parts_name(part_name_1, part_name_2)
    else:
        students = await api.get_students_by_one_part_name(words[0])
        
    if len(students) == 0:
        return True, 'Не найдено ни одного студента.'
    
    answer = list()
    answer.append('Найдены следующие студенты:')

    page_size = 10
    j = 0
    
    for i in range(0, len(students)):
        if j == 0:
            answer.append(f'{i + 1}) {students[i]}')
        else:
            answer[-1] += f'\n{i + 1}) {students[i]}'
        
        j += 1
        j %= page_size
    
    return True, answer


async def handle_get_rating_student_by_name_command(message: str) -> tuple[bool, str]:
    words = message.split()
    
    if len(words) < 3:
        return False, 'Мне необходимо полное ФИО.'
    
    first_name = words[1]
    last_name = words[0]
    patronymic = ' '.join(words[2:])
    
    has_student = await api.has_student(first_name, last_name, patronymic)
    
    if not has_student:
        return True, 'Студент не найден.'
    
    return True, 'Студент найден.'


async def handle_unknow_command(message: str) -> tuple[bool, str]:
    return True, messages.not_understand_message
