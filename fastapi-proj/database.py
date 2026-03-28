from sqlalchemy import create_engine, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base

DATABASE_URL = 'postgresql:postgres:postgres//localhost/escola'

# Motor de comunicação com o banco de dados
engine = create_engine(DATABASE_URL)

# Gerenciador de sessões com o engine.
SessionLocal = sessionmaker(bind=engine)

# Classe pai das entidades dos bancos de dados.
Base = declarative_base()
