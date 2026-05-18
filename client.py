import socket

HOST = "127.0.0.1"
PORT = 5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def send_message(message):
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print("Server svarade:", response)

send_message("HELLO")
send_message("TIME")
send_message("DATE")
send_message("DATETIME")
send_message("BYE")

client_socket.close()