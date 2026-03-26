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
