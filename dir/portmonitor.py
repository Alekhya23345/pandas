from threading import Thread
import socket
host = str(input('host > '))
from_port = int(input('start scan from port > '))
to_port = int(input('finish scan from port> '))
counting_open = []
counting_close = []
threads = []
class Finding_unsedports:
    def scan(port):
        s = socket.socket()
        result = s.connect_ex((str(host),port))
        if result == 0:
            counting_open.append(port)
            print((str(port))+' -> is open')
            peer = s.getpeername()
            print(peer)
            s.close()
        else:
            counting_close.append(port)
            s.close()
    for i in range(from_port, to_port+1):
        t = Thread(target=scan, args=(i,))
        threads.append(t)
        t.start()

    [x.join() for x in threads]

print(counting_open)
Finding_unsedports()