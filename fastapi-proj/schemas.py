from pydantic import BaseModel

class EstudanteBase(BaseModel):
    nome: str
    idade: int

class EstudanteCreate(EstudanteBase):
    pass

class EstudanteResponse(EstudanteBase):
    id: int # Note que o id não está no modelo base.
    class Config:
        # Fazer a leitura dos atributos diretamente do modelo base.
        from_attributes = True 

class MatriculaBase(BaseModel):
    estudante_id: int
    nome_disciplina: str

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int # Note que o id não está no modelo base.
    class Config:
        # Fazer a leitura dos atributos diretamente do modelo base.
        from_attributes = True 
