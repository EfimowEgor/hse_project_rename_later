class Student(object):
    def __init__(self, first_name, last_name, patronymic):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
