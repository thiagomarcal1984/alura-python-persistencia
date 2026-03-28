from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from database import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    nome = Column(
        String(100),
        nullable=False,
    )
    idade = Column(Integer)

class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    estudante_id = Column(
        Integer,
        ForeignKey('estudante.id'),
    )
    nome_disciplina = Column(
        String(100),
        nullable=False,
    )
