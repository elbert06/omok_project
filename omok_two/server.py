import socket
import sys
import time
bind_ip = "192.168.0.3"
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
socket.timeout(2)
m = []
print ("[*] Listening on %s:%d" , (bind_ip,bind_port))
client,addr = server.accept()
print ("[*] Accepted connection from: %s:%d" , (addr[0],addr[1]))
client.sendto(b"2", addr)
client2,addr2 = server.accept()
client2.sendto(b"1", addr2)
print ("[*] Accepted connection from: %s:%d" , (addr2[0],addr2[1]))
while True:
    request2 = client.recv(1024)
    request3 = str(request2,'utf-8')
    if request3 == "2":
        break
    client2.sendto(request2, addr2)
    request = client2.recv(1024)
    request4 = str(request,'utf-8')
    if request4 == "2":
        break
    client.sendto(request, addr)
sys.exit()
