#server.py
#!/usr/bin/python                           # This is server.py file

import socket                               # Import socket module

s = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 12345                                # Reserve a port for your service.
s.bind((host, port))                        # Bind to the port

s.listen(5)                                 # Now wait for client connections.
while True:
	c, addr = s.accept()                     # Establish connection with client.
	print('Got connection from', addr)


	flag = True

	while flag:


		print("Aguardando mensagem")


		data = c.recv(1024)
		print("Mensagem recebida: ",data.decode())

		if data.decode() == "SAIR":
			break

		msg = input("Digite a mensagem: ")
		c.send(msg.encode())

		if msg == "SAIR":
			c.send("SAIR".encode())
			flag = False
	

	
	print("Desconectando servidor")
	c.close()                                # Close the connection