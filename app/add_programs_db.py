from database import SessionLocal
from services.level_service import get_level_names
from services.program_service import create_program_from_parsed_data
from parse.parse_program import get_program_names_by_level


if __name__ == "__main__":
    db = SessionLocal()

    levels = get_level_names(db)

    print(levels)

    for level in levels:
        names = get_program_names_by_level(level)

        for name in names:
            try:
                program = create_program_from_parsed_data(db, name, level)
                print(f"Добавлена программа: {program.Name}")
            except ValueError:
                print(f"Ошибка: Уровень '{level}' не найден в базе данных.")
