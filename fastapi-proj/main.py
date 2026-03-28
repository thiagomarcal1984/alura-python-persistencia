from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
)
from sqlalchemy.orm import Session
from typing import List

import models
import schemas

from database import (
    engine,
    SessionLocal,
)

# Cria as tabelas no PostgreSQL (caso não existam).
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post(
    '/estudantes/', 
    # O modelo de resposta retorna um único registro.
    response_model=schemas.EstudanteResponse
)
def create_student(
    student: schemas.EstudanteCreate, # Wrapper dos dados do estudante.
    # `db` é um objeto do tipo `Session` que depende do retorno de `get_db`.
    db: Session = Depends(get_db), 
):
    # student.model_dump() é um dicionário com os campos da requisição POST.
    db_student = models.Estudante(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get(
    '/estudantes/',
    # O modelo de resposta retorna vários registros.
    response_model=List[schemas.EstudanteResponse],
)
def get(db: Session = Depends(get_db())):
    students = db.query(models.Estudante).all()
    return students
