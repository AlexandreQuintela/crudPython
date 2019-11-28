import sqlite3

conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM contato;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()