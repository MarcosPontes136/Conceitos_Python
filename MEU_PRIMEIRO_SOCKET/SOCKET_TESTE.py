import socket

resp = "S"
while (resp=="S"):
    url = input("Digite um url: ")
    ip = socket.gethostbyname(url)  #BUSCA IP
    print("O IP referente ao url informado é: ", ip)
    resp = input("Digite <S> para continuar: ").upper()
