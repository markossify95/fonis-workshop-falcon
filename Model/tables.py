from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from Model.dbconn import Base
from sqlalchemy import Column, Integer, String


class Prijava(Base):
    __tablename__ = 'prijava'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    predmet_id = Column(Integer, ForeignKey('predmet.id'), primary_key=True)
    ocena = Column(Integer, default=5)

    # predmet = relationship("Predmet")


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    predmeti = relationship("Predmet", secondary=Prijava.__table__, back_populates="studenti")

    # predmeti = relationship("Predmet")

    def __repr__(self):
        return "<Student(first_name='%s', last_name='%s')>" % (self.first_name, self.last_name)


class Predmet(Base):
    __tablename__ = 'predmet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    godina = Column(Integer, nullable=False)
    naziv = Column(String(30))
    studenti = relationship("Student", secondary=Prijava.__table__, back_populates="predmeti")

    def __repr__(self):
        return "<Predmet(godina='%s', naziv='%s')>" % (self.godina, self.naziv)
