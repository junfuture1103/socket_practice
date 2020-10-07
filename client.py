#this is client.py for socket practice
from socket import *
clientjunSock = socket(AF_INET, SOCK_STREAM)
clientjunSock.connect(('127.0.0.1', 8080))

print('야야야 연결했다. 메세지 보낼께')

msg = '야 내가 이준학이다'
clientjunSock.send(msg.encode('utf-8'))

recvdata = clientjunSock.recv(1024)
print('받은 데이터 : ', recvdata.decode('utf-8'))
