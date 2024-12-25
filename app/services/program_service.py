from database.models import Program
from services.level_service import get_level_id_by_name
from sqlalchemy.orm import Session


def create_program_from_parsed_data(db: Session, program_name: str, level_name: str):

    level_id = get_level_id_by_name(db, level_name)
    
    if not level_id:
        raise ValueError
    
    program = Program(Name=program_name, LvID=level_id)

    db.add(program)
    db.commit()
    db.refresh(program)

    return program

def get_programs(db: Session, program_name: str):
    pg = db.query(Program).filter(Program.Name == program_name).first()
    if pg:
        return pg.id
    else:
        raise ValueError
