#this is server.py for socket practice
from socket import *

serverjunSock = socket(AF_INET, SOCK_STREAM)
serverjunSock.bind(('', 8080))
serverjunSock.listen(1)
print('연결 기다리는 중.....')

connectjunSock, cilentaddr = serverjunSock.accept()
print('연결 왔다 이거')

msg = connectjunSock.recv(1024)
print(msg.decode('utf-8'))

serverjunSock.close()