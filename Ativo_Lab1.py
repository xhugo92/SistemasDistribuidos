import socket

HOST='localhost'
PORTA = 7000
sock= socket.socket()
sock.connect((HOST,PORTA))
print("Digite uma mensagem de Eco")
print("Digite 1 para finalizar")
while True:
    entrada = input()
    if(entrada=="1"):
        break
    sock.send(bytes(entrada,'utf-8'))
    msg = sock.recv(1024)
    print(str(msg, encoding= 'utf-8'))

sock.close()
