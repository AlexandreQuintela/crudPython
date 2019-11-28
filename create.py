import sqlite3
from Constroi import *

tela = Constroi
tela.titulo("Cadastro Contato")

conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
endereco = input('Endereco: ')
email = input('Email: ')
telefone = input('Telefone: ')

cursor.execute("""
INSERT INTO contato (nome, sobrenome, endereco, email, telefone)
VALUES (?,?,?,?,?)
""", (nome, sobrenome, endereco, email, telefone))

conn.commit()

tela.titulo("Dados inseridos com sucesso.")

conn.close()
