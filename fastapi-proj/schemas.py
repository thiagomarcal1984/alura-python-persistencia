from typing import List, Optional
from pydantic import BaseModel

class Perfil(BaseModel):
    class Config:
        # Fazer a leitura dos atributos diretamente do modelo base.
        from_attributes = True 
    id: int
    idade: int
    endereco: str

class PerfilCreate(BaseModel):
    # O id não aparece aqui porque não é necessário para criar um novo perfil.
    idade: int
    endereco: str

class Estudante(BaseModel):
    class Config:
        # Fazer a leitura dos atributos diretamente do modelo base.
        from_attributes = True

    id: int
    nome: str
    perfil: Optional[Perfil] = None

class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: PerfilCreate
