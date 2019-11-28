import sqlite3

conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

id_contato = input('Qual ID do contato que deseja Deletar?: ')


cursor.execute("""
DELETE FROM contatos
WHERE id = ?
""", (id_contato,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()