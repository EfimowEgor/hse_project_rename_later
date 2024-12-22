from database.models import Lv
from sqlalchemy.orm import Session


def get_level_id_by_name(db: Session, level_name: str):
    level = db.query(Lv).filter(Lv.Name == level_name).first()
    if level:
        return level.id
    else:
        raise ValueError
    
def get_level_names(db: Session):
    names = db.query(Lv.Name).all()
    return [name[0] for name in names]
