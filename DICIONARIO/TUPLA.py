ips={}
resp = "S"
while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),
        input("Digite os dois ultimos octetos: "))] = input("\nNome da maquina: ")
    resp=input("Digite <S> para continuar:\n ").upper()

    print("Exibir os ip's: ")
    for ip in ips.keys(): #.keys() = retorna todas as chaves em forma de lista.
        print(ip[0] + "." + ip[1])
