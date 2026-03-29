from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from database import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(
        Integer,
        primary_key=True,
        index=True, # Cria um índice no banco para esta coluna.
    )
    nome = Column(
        String(100),
        nullable=False,
    )
    email = Column(String)
    perfil = relationship(
        "Perfil", 
        back_populates="estudante",
        uselist=False, # O relacionamento será um para um, não um para muitos.
        cascade="all, delete-orphan",
    )

class Perfil(Base):
    __tablename__ = 'perfis'
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)
    estudante_id = Column(
        Integer, 
        ForeignKey("estudantes.id"),
        unique=True, # O campo estudante_id não pode ser repetido.
    )
    estudante = relationship(
        "Estudante", 
        back_populates="perfil",
        uselist=False,
    )

class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    estudante_id = Column(
        Integer,
        ForeignKey('estudantes.id'),
    )
    nome_disciplina = Column(
        String(100),
        nullable=False,
    )
