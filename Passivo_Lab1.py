import socket

HOST = ''
PORTA = 7000

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORTA))
sock.listen(1)
nsock, endereco = sock.accept()
while True:
    msg= nsock.recv(1024)
    if not msg:
        break
    print(str(msg, encoding='utf-8'))
    print("Enviando mensagem de volta")
    nsock.send(msg)
nsock.close()
sock.close()
