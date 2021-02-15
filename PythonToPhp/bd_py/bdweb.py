import mysql.connector #imprta o driver mysql
import os

mydb = mysql.connector.connect (

host = "datacenter_sql.mysql.dbaas.com.br",
user = "datacenter_sql",
password ="diegoj1dgl5",
database = "datacenter_sql"

)

sql4 = "SELECT nome, preco from produtos"
mycursor = mydb.cursor()

mycursor.execute(sql4)
for row in mycursor.fetchall():
    nome = row[0]
    preco = row[1]
    print(nome, preco)

#============================================================================================================

#Este documento faz conexão ao mysql remoto de uma hospedagem, as hospedagens que permitem conexão remota são em sua grande 
#maioria pagas, o exemplo acima está sendo feito com o uso do banco de dados de um antigo cliente cujo site está online 
#em uma hospedagem paga profdiegomat.com