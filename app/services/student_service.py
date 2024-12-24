from database.models import Students
from sqlalchemy.orm import Session


def create_user(db: Session, name, surname, patr):
    student = Students(Name=name, Surname=surname, Patronymic=patr)

    db.add(student)
    db.commit()
    db.refresh(student)

    return student

