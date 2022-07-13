import socket
ip = "211.243.158.233"
port = 9999
client = socket.socket()
client.connect((ip,port))
while True:
    m = input()
    client.send(m.encode())
    request = client.recv(1024)
    request1 = str(request,'utf-8')
    print (request1)