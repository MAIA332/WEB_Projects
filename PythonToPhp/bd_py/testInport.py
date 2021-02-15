from classeBD import conncetToBd
import mysql.connector #imprta o driver mysql

conexao = conncetToBd()

mydb = conexao.conectar('localhost','root', '', 'dolphindb')

myc = conexao.select_all('video_', mydb)

print(myc)