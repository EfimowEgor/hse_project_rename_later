from database import SessionLocal
from services.student_service import create_user
import asyncio
from parse.parse_names import main


def process_name_string(db, fio_string):
    parts = fio_string.split()
    if len(parts) < 2:
        print(f"Invalid FIO string format: {fio_string}")
        return None

    name = parts[1]
    surname = parts[0]

    if len(parts) >= 3:
        patronymic = " ".join(parts[2:])
        usr = create_user(db=db, name=name, surname=surname, patr=patronymic)
    elif len(parts) == 2:
        usr = create_user(db=db, name=name, surname=surname, patr=None)

    return usr

async def run_parser():
    fio_set = await main()
    db = SessionLocal()
    try:
        for fio in fio_set:
            process_name_string(db, fio)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    asyncio.run(run_parser())