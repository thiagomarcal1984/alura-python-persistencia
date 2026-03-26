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
