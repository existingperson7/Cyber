# android server

import socket
import time

HOST = "0.0.0.0"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Waiting for Android connection...")

while True:
    client, address = server.accept()

    print("Android connected:", address)

    data = client.recv(1024).decode("utf-8")
    print("Received:", data)

    print("Waiting 3 seconds...")
    time.sleep(3)

    answer = "1"

    client.sendall((answer + "\n").encode("utf-8"))

    print("Answer sent!")

    client.close()