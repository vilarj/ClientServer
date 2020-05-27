import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP Protocol
skt.bind((socket.gethostname(), 1234))
skt.listen(5)

while True:
    clt, address = skt.accept()
    print(f"{address} just connected")
    clt.send(bytes("Socket Programming in Python", "UTF-8"))