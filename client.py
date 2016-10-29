import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("ipb.ac.id",80))
s.send(b'GET / HTTP/1.1\nHost: ipb.ac.id\n\n')
datafromserver = s.recv(4096)

print("Server response: " + str(datafromserver))

s.close()
