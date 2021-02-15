# coding: utf-8

from ftplib import FTP
import logging

# A função baixa um arquivo definido por 'filename' na pasta Downloads com o nome
# especificado por 'name'
def download(handler, name, filename="Uploads/musica1.mp3"):
    Dfile = open('PastaExemplo/Downloads/' + name, 'wb')

    try:
        handler.retrbinary('RETR ' + filename, Dfile.write)
    except Exception:
        raise    



    Dfile.close()
    logging.info('Dowload feito com sucesso! ')

# a função conecta um cliente no servidor
# é chamado assim que a linha de comando é iniciada
def connectClient():

    try:
        ftp = FTP('ftpupload.net')
        ftp.login(user='epiz_26113659', passwd = '5mFQoWfwv6')
        logging.info('Conectado ao servidor =)')
    except Exception:
        logging.critical('Não foi possivel conectar ao servidor FTP')

    return ftp


# a função sobe um arquivo no servidor com o nome especificado por 'name'
# localizada no diretório espeficidado por 'path'
def upload(ftp, filename):

    try:
        file = open(filename,'rb')                  # file to send
        ftp.storbinary('STOR'+ filename, file)     # send the file
        file.close()    
    except Exception:
        return None

    logging.info('upload feito com sucesso')

# A função move o cliente para o diretório determinado por Dir
def moveToDir(ftp, Dir):

    try:
        ftp.cwd(Dir)
    except Exception:
        print ('Não foi possivel acessar o diretorio ou o diretorio não existe')


# A função cria um novo diretório com o nome especificado por 'name'
def makeDir(handler, name):

    try:
        handler.mkd(name)
    except Exception:
        print ('Não foi possivel criar o diretorio =( ')

# A função deleta um arquivo com o nome especificado por 'name'
def delFile(handler, name):

    try:
        handler.delete(name)
    except Exception:
        print (' não foi possivel deletar o arquivo ou ele é inexistente')