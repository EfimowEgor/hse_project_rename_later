from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Lv(Base):
    __tablename__ = "Lv"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)

    programs = relationship("Program", back_populates="lv")


class Types(Base):
    __tablename__ = "Types"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)

    stats = relationship("Stats", back_populates="type")


class Program(Base):
    __tablename__ = "Program"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    LvID = Column(Integer, ForeignKey("Lv.id"))

    lv = relationship("Lv", back_populates="programs")

    students = relationship("Students", back_populates="program")


class Students(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    Surname = Column(String, nullable=False)
    Patronymic = Column(String, nullable=True)

    stats = relationship("Stats", back_populates="student")


class Stats(Base):
    __tablename__ = "Stats"

    id = Column(Integer, primary_key=True, index=True)
    StudentID = Column(Integer, ForeignKey("Students.id"))
    Rating = Column(String, nullable=True)
    MeanGrade = Column(DECIMAL(4, 2), nullable=True)
    MinGrade = Column(DECIMAL(5, 2), nullable=True)
    Percentile = Column(DECIMAL(5, 2), nullable=True)
    GPA = Column(DECIMAL(4, 2), nullable=True)
    Course = Column(Integer, nullable=True)
    Years = Column(String, nullable=True)
    TypeID = Column(Integer, ForeignKey("Types.id"))
    MODULES = Column(String, nullable=True)
    ProgramID = Column(Integer, ForeignKey("Program.id"))

    program = relationship("Program", back_populates="students")
    student = relationship("Students", back_populates="stats")

    type = relationship("Types", back_populates="stats")
