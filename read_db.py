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
