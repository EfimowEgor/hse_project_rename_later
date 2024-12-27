class Student(object):
    def __init__(self, first_name, last_name, patronymic):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class StudentRating(object):
    def __init__(self, program_name, course, years, modules, place, mean_grade, min_grade, percentile, gpa):
        self.program_name = program_name
        self.course = course
        self.years = years
        self.modules = modules
        self.place = place
        self.mean_grade = mean_grade
        self.min_grade = min_grade
        self.percentile = percentile
        self.gpa = gpa
    
    def __str__(self):
        return f'Учебный год:\t{self.years}\nМодули:\t{self.modules}\nСредняя оценка:\t{self.mean_grade}\n' \
            + f'Минимальная оценка:\t{self.min_grade}\nПерцентиль:\t{self.percentile}\nМесто:\t{self.place}'
