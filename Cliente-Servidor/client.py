
#client.py

#!/usr/bin/python                      # This is client.py file

import socket                          # Import socket module

s = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345                           # Reserve a port for your service.

s.connect((host, port))

flag = True

while flag:
	
	msg = input("Digite mensagem: ")
	s.send(msg.encode())

	if msg == "SAIR":
		break

	print("Aguardando mensagem..")
	data = s.recv(1024)
	print("Mensagem recebida: ",data.decode())

	if data.decode() == "SAIR":
		flag = False
		s.send("SAIR".encode())

print("Desconectando Client...")
s.close()    