import socket
import os
import sys
HOST = '10.6.2.209'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    pid = os.fork()
    if pid == 0:
        tcp.close()
        print ('Conectado por', cliente)
        while True:
            msg = con.recv(1024)
            if not msg: break
            print (cliente, msg)
        print ('Finalizando conexao do cliente', cliente)
        con.close()
        sys.exit(0)
    else:
        con.close()