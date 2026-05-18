import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Servern väntar på anslutning...")

connection, address = server_socket.accept()
print("Klient ansluten:", address)

while True:
    message = connection.recv(1024).decode()

    if message == "HELLO":
        response = "WELCOME"

    elif message == "TIME":
        response = "TIME|" + datetime.now().strftime("%H:%M:%S")

    elif message == "DATE":
        response = "DATE|" + datetime.now().strftime("%Y-%m-%d")

    elif message == "DATETIME":
        response = "DATETIME|" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    elif message == "BYE":
        response = "GOODBYE"
        connection.send(response.encode())
        break

    else:
        response = "ERROR|Unknown command"

    connection.send(response.encode())

connection.close()
server_socket.close()
print("Servern är stängd.")