import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:

	servidor.bind((HOST, PORT))
	
	servidor.listen()
	print(f"Server escutando em {HOST}:{PORT} e aguardando conexões...")

	sock_cliente, endereco_cliente = servidor.accept()
	with sock_cliente:
		print(f"Conexão estabelecida com {endereco_cliente}")

		while True:
			
			dados = sock_cliente.recv(1024)
			
			if not dados:
				print("Cliente desconectou")
				break

			print(f"Mensagem recebida: {dados.decode()}")
			sock_cliente.sendall(dados)
