import socket
from _thread import *

#membuat socket/(analogi telp)

def clientthread(conn):
    datafromclient = conn.recv(100) #blocking
    print("Says " + str(datafromclient))
    conn.send(b'hello I am HK\n')
    conn.close()

host = ""
port = 2000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("server listening on port " + str(port))

s.listen(10)

while 1:
    conn, addr = s.accept()
    print("incoming connection from " + str(addr))

    start_new_thread(clientthread,(conn,))
   

s.close()
