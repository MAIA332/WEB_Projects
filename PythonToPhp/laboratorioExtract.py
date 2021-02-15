#!/usr/bin/env python

import mysql.connector #imprta o driver mysql
import os
import PySimpleGUI as sg


mydb = mysql.connector.connect (

host = "localhost",
user = "root",
password ="",
database = "dolphindb"

)

class TelaPython:
    def __init__(self):

        sg.change_look_and_feel('SystemDefaultForReal') #estilo

        # layout ===============================
        layout = [
            [sg.Text('=======================')],
            [sg.Text('Gênero', size=(5, 0)), sg.Input(size=(15, 0), key='genero')],
            [sg.Text('Ator', size=(5, 0)), sg.Input( size=(15, 0), key='ator')],
            [sg.Text('Compositor', size=(8, 0)), sg.Input( size=(15, 0), key='compositor')],
            [sg.Text('Titulo', size=(5, 0)), sg.Input( size=(15, 0), key='titulo')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30,20))]
        ]
        # janela ===========
        self.janela = sg.Window("Inserir novo video").layout(layout)

    def iniciar(self):
        # print(self.values)

        while True:
            # extrair os dados da tela

            self.button, self.values = self.janela.Read()

            genero = self.values['genero']
            ator = self.values['ator']
            compositor = self.values['compositor']
            titulo = self.values['titulo']
            
            print(f'Dados inseridos com sucesso! ')
            print(f'=====================')
            print(f'Genero: {genero}')
            print(f'Ator: {ator}')
            print(f'compositor: {compositor}')
            print(f'titulo: {titulo}')
            print(f'=====================')

            sql2 = "CALL add_video(%s,%s,%s,%s)"

            mycursor = mydb.cursor()

            mycursor.execute(sql2, (genero, ator, compositor, titulo))

            mydb.commit()




tela = TelaPython()
tela.iniciar()