# Fazer o servidor multithreads.
import socket
from time import sleep
import threading
from funcoesDeGerenciamento.GereciadorDeFuncoes import *

HOST = '0.0.0.0'
PORT = 65432
#criando o socket, com protocolo UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((HOST, PORT))
print('Servidor no ar... Faça seu pedido')

status = {
    "OK": "200-OK",
    "EXIT": "150-CUSTOMER LEFT",
    "ERROR": "100-ERROR"
}

try:
    while True:
        msg, cliente = udp.recvfrom(1024)
        print(f'Cliente',cliente)
        print('Comando',msg.decode())
        print('Chamando a thread de tratamento')
        thread_de_tratamento = threading.Thread(target=trata_cliente, args=(udp,msg, cliente,))
        sleep(1)
        thread_de_tratamento.start()

except:
    udp.sendto('Servidor Caiu!!'.encode(),cliente)

