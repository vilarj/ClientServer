import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 1234))

message = client.recv(1234)
print(message.decode("UTF-8"))