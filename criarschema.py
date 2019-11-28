import sqlite3

conn = sqlite3.connect('agenda.db')

cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE contato (
        id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome       TEXT NOT NULL,
        sobrenome  TEXT NOT NULL,
        endereco   VARCHAR(100) NOT NULL,
        telefone   TEXT NOT NULL,
        email      TEXT NOT NULL
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()