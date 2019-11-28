import sqlite3

conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

id_contato = input('Qual ID do contato que deseja Alterar?: ')
novo_fone = '11-1000-2014'
novo_email = "lolo@lolo.com"

cursor.execute("""
UPDATE contatos
SET telefone = ?, email = ?
WHERE id = ?
""", (novo_fone, novo_email, id_contato))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()