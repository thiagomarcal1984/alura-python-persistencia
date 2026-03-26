import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute(
    """
        SELECT * FROM estudantes
    """
)

# Recuperação do que o cursor executou.
estudantes = cursor.fetchall()

[ print(estudante) for estudante in estudantes ]

conn.close()
