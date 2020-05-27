import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP Protocol
skt.bind((socket.gethostname(), 1234))
skt.listen(5)

while True:
    communicate, address = skt.accept()
    print(f"{address} just connected✔")
    communicate.send(bytes("Socket Programming in Python", "UTF-8"))

    communicate.close()
