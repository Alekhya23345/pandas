import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind((socket.gethostname(), 1347))    # 0-65535 Unique port number
sk.listen()
while True:
    client, address = sk.accept()
    print("Connection Established")
    print(address)
    client.send(b"socket Programming")

