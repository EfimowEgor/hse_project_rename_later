from database.models import Stats
from sqlalchemy.orm import Session

def create_stats(db: Session, studID, rating, gmean, gmin, percentile, gpa, course, years, typeid, modules, pgID):
    stats = Stats(StudentID=studID, 
                  Rating=rating,
                  MeanGrade=gmean,
                  MinGrade=gmin,
                  Percentile=percentile,
                  GPA=gpa,
                  Course=course,
                  Years=years,
                  TypeID=typeid,
                  MODULES=modules,
                  ProgramID=pgID)

    db.add(stats)
    db.commit()
    db.refresh(stats)

    return stats