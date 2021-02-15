import ftp_in as fl

trigger = 0
sep = '==============================================='

while trigger == 0:
    print(sep)
    ht = input('Nome do diretorio no servidor: ')
    print(sep)
    filen = input('Nome do arquivo em seu computador com extensao: ')
    print(sep)
    trigger = 1

try:
    conn = fl.connectClient()
    fl.moveToDir(conn, ht)
    fl.upload(conn, filen)
    print("upload granted")
except Exception:
    print("Not connect")