import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect((socket.gethostname(),1347))
msg = sk.recv(1024)
print(msg.decode("utf-8"))