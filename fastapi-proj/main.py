from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
)
from sqlalchemy import select
from sqlalchemy.orm import joinedload, Session
from typing import List

import models
import schemas

from database import (
    engine,
    SessionLocal,
)

# Cria as tabelas no PostgreSQL (caso não existam).
# Lembre-se que o comando não vai funcionar se o banco de dados não existir.
models.Base.metadata.drop_all(bind=engine)
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
    response_model=schemas.Estudante
)
def create_student(
    estudante: schemas.EstudanteCreate, # Wrapper dos dados do estudante.
    # `db` é um objeto do tipo `Session` que depende do retorno de `get_db`.
    db: Session = Depends(get_db), # Não invoque a função get_db.
):
    # student.model_dump() é um dicionário com os campos da requisição POST.
    db_estudante = models.Estudante(
        nome = estudante.nome,
        email = estudante.email,
        # perfil = models.Perfil(**estudante.perfil.dict()),
        perfil = models.Perfil(**estudante.perfil.model_dump()),
        # perfil = models.Perfil(**estudante.perfil.__dict__),
    )
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante

@app.get(
    '/estudantes/',
    # O modelo de resposta retorna vários registros.
    response_model=List[schemas.Estudante],
)
def get(db: Session = Depends(get_db)): # Não invoque a função get_db.
    # # Legado
    # estudantes = db.query(models.Estudante).options(
    #     joinedload(models.Estudante.perfil)
    # ).all()

    # Tentativa com notação nova.
    estudantes = db.scalars(select(models.Estudante).options(
        joinedload(models.Estudante.perfil) # Eager loading, para eficiência.
    )).all()
    return estudantes
