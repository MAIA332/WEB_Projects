#!/usr/bin/env python

import mysql.connector #imprta o driver mysql
import os



try:
    mydb = mysql.connector.connect (

    host = "192.168.15.55", #ip do coputador onde o acesso foi autorizado
    user = "root", #usuario configurado
    password =" ",# senha configurada, note que aqui a senha e um espaco, e não vazia,  note tambem que essa senha é exclusiva para esse ip que está solicitando acesso
    database = "dolphindb"# banco de dados a ser acessado

    )
    sql2 = "INSERT INTO dolphin1(nome) values('Maia')"

    mycursor = mydb.cursor()

    mycursor.execute(sql2)

    mydb.commit()
    print("Connected")
except :
    print("N foi possivel realizar a conezao com o banco")