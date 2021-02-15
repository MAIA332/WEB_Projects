#!/usr/bin/env python

import mysql.connector #imprta o driver mysql
import os

class conncetToBd:

    def conectar(self, host, user, password, database):
        try:
            mydb = mysql.connector.connect (

            host = host,
            user = user,
            password =password,
            database = database

            )
            return mydb 
        except:
            print("N foi possivel realizar a conezao com o banco")
    
    def select_all(self, table, mydb ):

        try:

            sql2 = "SELECT * FROM %s"
            
            mycursor = mydb.cursor()

            mycursor.execute(sql2,(table,))

            myresult = mycursor.fetchall()

            return myresult
        except:
            print("N deu")


