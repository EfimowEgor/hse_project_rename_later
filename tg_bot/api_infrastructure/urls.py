from config import student_api_url

has_student_url = student_api_url + '/students/has'
get_students_by_one_part_name_url = student_api_url + '/students/one_part_name'
get_students_by_two_parts_name_url = student_api_url + '/students/two_parts_name'

get_current_student_ratings_by_name_url = student_api_url + '/students/ratings/current'
get_after_retake_student_ratings_by_name_url = student_api_url + '/students/ratings/after_retake'
get_cumulative_student_ratings_by_name_url = student_api_url + '/students/ratings/cumulative'
