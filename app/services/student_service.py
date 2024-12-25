from database.models import Students
from sqlalchemy.orm import Session
from sqlalchemy import and_


def process_name_string(fio_string):
    parts = fio_string.split()
    if len(parts) < 2:
        raise ValueError(f"Invalid FIO string format: {fio_string}")

    name = parts[1]
    surname = parts[0]

    if len(parts) >= 3:
        patronymic = " ".join(parts[2:])
    elif len(parts) == 2:
        patronymic = None

    return name, surname, patronymic


def create_user(db: Session, name, surname, patr):
    student = Students(Name=name, Surname=surname, Patronymic=patr)

    db.add(student)
    db.commit()
    db.refresh(student)

    return student

def get_users(db: Session, stud_name: str):
    name, surname, patronymic = process_name_string(stud_name)

    user = db.query(Students).filter(
        and_(
            Students.Name == name,
            Students.Surname == surname,
            Students.Patronymic == patronymic if patronymic is not None else Students.Patronymic.is_(None)
        )
    ).first()

    if user:
        return user.id
    else:
        raise ValueError(f"Пользователь с именем '{stud_name}' не найден.")
