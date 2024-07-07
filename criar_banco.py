import sqlite3


#conexão com o banco
connection = sqlite3.connect('')

#criando um cursor e para selecionar as coisas no banco de dados.
cursor= connection.cursor()

#script que cria tabela ou outros

cria_tabela= "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
    nome text, estrelas real, diaria real, cidade text)"

#script que inseri no banco de dados

inserir_dados = "INSERT INTO hoteis VALUES ('alpha','Alpha Hotel', 4.3, 345.30, 'Rio de Janeiro')"

cursor.execute(cria_tabela)

cursor.execute(inserir_dados)

connection.commit()
connection.close()
 