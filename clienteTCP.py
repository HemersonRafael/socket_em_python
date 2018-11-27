# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:39:29 2018

@author: hduser

"""

import socket
HOST = '10.6.1.228'     # Endereco IP do Servidor
PORT = 65433            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))
print ('Para sair use CTRL+X\n')
msg = bytes(input("Informe a mensagem: "),'utf-8')

while (msg != b'\x18'):
    tcp.send (msg)
    msg = bytes(input("Informe a mensagem: "),'utf-8')
tcp.close()


#!/usr/bin/env python3

"""
import socket

HOST = '10.6.2.209'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
msg = input()
msg = bytes(msg,'utf-8')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(msg)
    data = s.recv(1024)
    s.close()
print('Received', repr(data))
"""