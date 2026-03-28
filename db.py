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
        CREATE TABLE IF NOT EXISTS matriculas (
            id INTEGER PRIMARY KEY, 
            nome_disciplina TEXT,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
        )
    ''')
    conn.commit()
    conn.close()

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
