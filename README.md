# Listas, Tuplas e Dicionários
## Características e declaração de uma lista
Listas são 1) ordenadas e 2) mutáveis.

```python
# Lista vazia
lista = []
lista
# Saída: 
# [] 

lista = [1, 'python', 2]
lista
# Saída: 
# lista = [1, 'python', 2]

# Acesso a um elemento específico da lista:
lista[0]
# Saída: 
# 1
lista[2]
# Saída: 
# 2

# Alterando um item da lista:
lista[0] = 'Alterado'
lista
# Saída: 
# ['Alterado', 'python', 2]
```
## Adicionando elementos na lista
1. Usando o método `append`:
```python
lista = ['Alterado', 'python', 2]
lista.append('novo elemento')
lista
# Saída:
# ['Alterado', 'python', 2, 'novo elemento']
```
2. Usando o método `insert` (com dois parâmetros, sendo o primeiro a posição na lista e o segundo o elemento a ser inserido):
```python
lista = ['Alterado', 'python', 2, 'novo elemento']
lista.insert(0, 'Elemento zero')
lista
# Saída: 
# ['Elemento zero', 'Alterado', 'python', 2, 'novo elemento']
```

## Trabalhando com tuplas
Tuplas são 1) ordenadas e 2) imutáveis.

Note que listas também são ordenadas, mas são mutáveis. Tuplas não mudam.

```python
# Declarando uma tupla:
t = 123, 234, 'oi'
t
# Saída:
# (123, 234, 'oi')

# Acessando um elemento da tupla:
t[2]
# Saída: 
# 'oi'

t[1] = 'alterado'
# Saída: TypeError: 'tuple' object does not support item assignment
t.append('alterado')
# Saída: AttributeError: 'tuple' object has no attribute 'append'

# Criando uma tupla aninhada:
v = t, lista
type(v)
# Saída: <class 'tuple'>
v
# Saída: 
# ((123, 234, 'oi'), ['Alterado', 'python', 2, 'novo elemento'])
# Note que é uma tupla de dois elementos, sendo o primeiro uma tupla aninhada e o segundo uma lista.
```

> Note que para criar uma tupla os parênteses são opcionais:
> ```python
> tupla = 123, 234, 'oi'
> ```

## Explorando dicionários
* Dicionários são 1) não ordenados e 2) mutáveis. 
* Diferente de tuplas, dicionários são mutáveis. 
* Diferente das listas, dicionários não são ordenados.
* Dicionários funcionam como um mapeamento/armazenamento de par chave/valor.
* Dicionários são muito usados para criar arquivos no formato JSON.

```python
# Criando um dicionário:
telefones = {
    'joao': 911112222,
    'leo' : 933334444
}
telefones
# Saída:
# {'joao': 911112222, 'leo': 933334444}

# Acessando um item do dicionário `telefones` a partir da chave `joao`:
telefones['joao']
# Saída: 
# 911112222

# Acrescentando um item chave/valor ao dicionário `telefones`:
telefones['elena'] = 955556666
telefones
# Saída: 
# {'joao': 911112222, 'leo': 933334444, 'elena': 955556666}
```

## Técnicas de iteração
Declaração das variáveis necessárias aos exemplos:
```python
lista = ['Elemento zero', 'Alterado', 'python', 2, 'novo elemento']
v = ((123, 234, 'oi'), ['Alterado', 'python', 2, 'novo elemento'])
telefones = {'joao': 911112222, 'leo': 933334444, 'elena': 955556666}
```
1. Iterando com o loop for sobre uma lista ou uma tupla:
```python
for i in lista:
    print(i)
    
for i in v:
    print(i)
```

2. Iterando com o loop for sobre uma dicionário:
```python
# Iterando sobre as chaves usando o método `.keys()`
for chave in telefones.keys():
    print(f'K: {chave}')

# Iterando sobre os valores usando o método `.values()`
for valor in telefones.values():
    print(f'K: {valor}')

# Iterando sobre os itens usando o método `.items()`
for chave, valor in telefones.items():
    print(f'K: {chave}; V: {valor}')
```
> Note que, ao iterar sobre um dicionário usando método `.items()` as variáveis temporárias do loop são duas ao invés de uma. São duas por causa do par chave/valor.

# Gravação e Manipulação de arquivos
## Lidando com arquivos txt
A função `open`, usada para criar, ler e escrever arquivos, possui dois parâmetros:

1. o nome do arquivo; e 
2. o modo de interação com o arquivo (`r` para leitura, `w` para escrita etc.).

```python
# escrever um arquivo com a função open()
with open('dados.txt', 'w') as f:
    f.write('Olá, mundo') # Retorna o número de chars escritos.

# lendo um arquivo INTEIRO.
with open('dados.txt', 'r') as f:
    print(f.read())
```

## Gravando e manipulando arquivos csv
```python
with open('dados.txt', 'a') as f: # `a` é o modo de append.
    f.write('ultima linha')
```

Para gravar/ler csv, usamos os construtores `writer` ou `reader` do módulo `csv`:
```python
import csv

# Escrevendo o arquivo csv.
with open('dados.csv', 'w', newline='') as f:
    # Ao fornecer `newline=''`, evitamos a inserção de uma linha
    # adicional a cada escrita com o método `escritor.writerow`.
    escritor = csv.writer(f) # Não se esqueça de fornecer o arquivo.
    escritor.writerow(['nome', 'idade'])
    escritor.writerow(['Ana', '32'])

# Lendo o arquivo csv.
with open('dados.csv') as f: 
    leitor = csv.reader(f) # Não se esqueça de fornecer o arquivo.
    for linha in leitor:
        print(linha) # Imprime a lista correspondente ao conteúdo da linha.
```
## Criando e modificando arquivos json
Assim como com o CSV, o trabalho sobre arquivos JSON dependem de um módulo próprio (no caso, `json`). 

O método para escrever dados no formato json é `json.dump`.

```python
import json

dados = {
    'nome': 'Ana',
    'idade': 32,
    'enderecos': ['a', 'b'],
}

# Escrevendo o json com `json.dump`:
with open('dados.json', 'w') as f:
    json.dump(dados, f)

# Lendo o json com `json.load`:
with open('dados.json') as f:
    dados_lidos = json.load(f)
    print(dados_lidos)
```
> Problemas com o uso de arquivos:
> 1. Não possuem estrutura relacional;
> 2. Dificuldade na busca;
> 3. Problemas na concorrência;
> 4. Falta de segurança e integridade;
> 5. Escalabilidade.

## Praticando a leitura e escrita de arquivos
Exercício para escrita de arquivos:
```python
# input_data.py
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

with open('input_data.txt', 'a') as f:
    f.write(f'Nome: {nome}\n')
    f.write(f'Idade: {idade}\n')
```
Exercício para leitura de arquivos:
```python
# read_data.py
with open('input_data.txt', 'r') as f:
    for linha in f:
        print(linha)
```

# Banco de dados
## Entendendo o que é um banco de dados
- Bancos SQL (relacionais): os dados são organizados em linhas de tabelas;
- Bancos NoSQL (não relacionais): os dados são organizados como dicionários/mapas.

| Característica | SQL (Relacional) | NoSQL (Não Relacional)
|-|-|-
| Modelo de dados | Tabela com colunas fixas | Documentos, chave-valor
| Esquema (ex. colunas/campos) | Rígido |Flexível
| Relacionamentos | Nativo | Embutido ou manuais
| Exemplos de uso | ERPs, bancos | Apps web, redes sociais

## Bancos de dados relacionais
Conceitos chave:
- Tabela
- Linha
- Coluna
- Chave primária
- Chave estrangeira
- Relacionamentos
    - 1:1
    - 1:N
    - N:N

Usando Python:
```python
# db_sql.py
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudantes(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
''')

cursor.execute(
    'INSERT INTO estudantes (nome, idade) VALUES (?, ?)',
    ("Joao", 20)
)

conn.commit()

cursor.execute('SELECT * FROM estudantes')
print(cursor.fetchall())

conn.close()
```
## Bancos de dados não relacionais
Conceitos de bancos de dados não relacionais:
- Documento
- Coleção (agrupamento de entradas que referenciam os documentos)
- ID (cada entrada tem um)
- Relacionamentos embutidos

```python
# db_mongo.py
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['escola']
estudantes = db['estudantes']

estudantes.insert_one({
    'nome': 'João', 
    'idade': 20, 
})

for estudante in estudantes.find():
    print(estudante)
# Saída: {'_id': ObjectId('69c08c2878aa769178e524ee'), 'nome': 'João', 'idade': 20}
```

# Manipulação de Dados com SQL em SQLite
## Comandos básicos
Os comandos do SQLite não são diferentes do SQL. Comandos como `CREATE TABLE`, `INSERT INTO`, `SELECT` etc.

No curso criaremos duas entidades: disciplinas e estudantes.

## Como manipular dados com SQL
Criando as tabelas com SQLite:
```Python
# create_db.py
import sqlite3

# Cria o banco (caso não exista) e conecta com ele.
conn = sqlite3.connect('escola.db')

# Cria o cursor que vai processar os comandos SQL.
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudantes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY,
        nome_disciplina TEXT, 
        estudante_id INTEGER,
        FOREIGN KEY (estudante_id) 
            REFERENCES estudantes(id)
    )
""")

# Confirmar a criação das tabelas.
conn.commit()
```
## Como escrever e ler dados no DB
Código de escrita no banco:
```python
# write_db.py
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO estudantes(nome, idade) VALUES (?, ?)",
    ("Joana", 16) # Parâmetros para evitar SQL Injection.
)

conn.commit()
conn.close()
```

Código de leitura no banco:
```python
# read_db.py
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudantes")

# Recuperação do que o cursor executou.
estudantes = cursor.fetchall()

[ print(estudante) for estudante in estudantes ]

conn.close()
```
## Praticando a manipulação de dados com SQL
Atualizando o banco:
```python
# update_db.py
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute(
    "UPDATE estudantes SET nome = ? WHERE id = ?",
    ("Leandro", 2)
)

conn.commit()
conn.close()
```

Criando uma disciplina:
```python
# write_db.py
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# cursor.execute(
#     """
#         INSERT INTO estudantes(nome, idade) \
#         VALUES (?, ?)
#     """,
#     ("Joana", 16)
# )

cursor.execute(
    """
        INSERT INTO disciplinas(estudante_id, nome_disciplina) \
        VALUES (?, ?)
    """,
    (1, "Matemática")
)

conn.commit()
conn.close()
```

Lendo a tabela de disciplinas:
```python
# read_db.py
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# cursor.execute("SELECT * FROM estudantes")
# estudantes = cursor.fetchall()
# [ print(estudante) for estudante in estudantes ]

cursor.execute("SELECT * FROM disciplinas")
disciplinas = cursor.fetchall()
[ print(disciplina) for disciplina in disciplinas ]

conn.close()
```
## Realizando consultas e boas práticas

```python
import sqlite3
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM estudantes WHERE id = 1')
estudante = cursor.fetchall()
print(estudante)

cursor.execute("""
    SELECT estudantes.nome, disciplinas.nome_disciplina
    FROM disciplinas
    JOIN estudantes ON disciplinas.estudante_id = estudantes.id
""")

print(cursor.fetchall())
```
Boas práticas:
* Use `?` para passar parâmetros;
* Use `IF NOT EXISTS` ao criar tabelas;
* Use `conn.commit()` para confirmar atualizações no banco;
* Use `conn.close()` para fechar a conexão e liberar recursos.

# Integração do Python com SQLite
## Criando uma estrutura basica
Script para criação das tabelas:
```python
# db.py
import sqlite3

def conectar():
    conn = sqlite3.connect('escola.db')
    return conn

def criar_tabela_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT, 
            idade INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_matricula():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matriculas(
            id INTEGER PRIMARY KEY, 
            nome_disciplina TEXT,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
        )
    ''')
    conn.commit()
    conn.close()
```
## Manipulando o banco de dados
Mais funções no arquivo `db.py`:
```python
# db.py

# Resto do código
def criar_estudante(nome, idade):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
                INSERT INTO estudantes (nome, idade)
                VALUES (?, ?)
            """,
            (nome, idade)
        )
        conn.commit()

def listar_estudantes():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM estudantes")
        estudantes = cursor.fetchall()
        [ print(estudante)  for estudante in estudantes ]
```
## Demonstrando a manipulação do DB
Um caminho para carregar as funções de um arquivo após entrar no interpretador Python:
```shell
>>> exec(open('db.py').read())
```
Agora as funções todas estão importadas no interpretador.

Vamos continuar usando o interpretador:
```python
>>> criar_tabela_estudantes()
>>> criar_tabela_matricula() 
>>> criar_estudante("Luana", 20)
>>> listar_estudantes()
# Saída:
(1, 'Luana', 20)
>>> criar_estudante("Lucas", 22)
>>> listar_estudantes()
# Saída:
(1, 'Luana', 20)
(2, 'Lucas', 22)
```
## Praticando o uso do Python e SQLite
Alterações no arquivo `db.py`:
```python
# db.py

# Resto do código
def criar_matricula(estudante_id, nome_disciplina):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
                INSERT INTO matriculas (estudante_id, nome_disciplina)
                VALUES(?,?)
            """,
            (estudante_id, nome_disciplina)
        )
        conn.commit()

def listar_matriculas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM matriculas")
        matriculas = cursor.fetchall()
        [ print(matricula) for matricula in matriculas ]
```

Executando os comandos após a alteração do arquivo `db.py`:
```python
>>> exec(open('db.py').read())
>>> criar_matricula(1, 'Matemática')
>>> listar_matriculas()
# Saída:
(1, 'Matemática', 1)
```

## Utilizando o comando JOIN
Vamos mudar a função `listar_matriculas` para juntar duas tabelas no resultado:
```python
# db.py

# Resto do código
def listar_matriculas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
                SELECT matriculas.id, estudantes.nome, matriculas.nome_disciplina
                FROM matriculas
                JOIN estudantes ON matriculas.estudante_id = estudantes.id
            """
        )
        matriculas = cursor.fetchall()
        [ print(matricula) for matricula in matriculas ]
```

Executando os comandos após a alteração do arquivo `db.py`:
```python
>>> exec(open('db.py').read())
>>> listar_matriculas()
# Saída:
(1, 'Luana', 'Matemática')

>>> criar_matricula(2, "História")
>>> listar_matriculas()
# Saída:
(1, 'Luana', 'Matemática')
(2, 'Lucas', 'História')
```
# Persistência com PostgreSQL e FastAPI
## Instalando dependências
Instale as dependências do PIP usando o arquivo [requirements.txt](requirements.txt). 

```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Estruturando o projeto com database.py
Quatro arquivos serão criados para o subprojeto do diretório `fastapi-proj`:
1. `database.py` vai realizar as operações com o banco de dados;
2. `main.py` vai definir as rotas e endpoints da API;
3. `models.py` vai definir os modelos de entidades mapeados com o banco;
4. `schemas.py` vai definir a validação dos modelos de banco de dados.

Começando com o código do `database.py`:
```python
# database.py
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
```
## Criando o models.py
```python
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
```
## Criando o schemas.py
```python
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
```
## Criando o main.py
```python
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
```
