usuario = {}
resp = "S"
emails=[]
while resp == "S":
    emails.append(input("Digite um e-mail: ").lower())
    resp=input("Digite <S> para continuar: ").upper()

    tupla = list(enumerate(emails))
    for chave in range(0, len(tupla)):
        print("Email: ", tupla[chave][1])
        usuario[tupla[chave]]=[input("Digite o nome: "), input("Digite o nivel: ")]

        for chave, dado in usuario.items():
            print("Usuario...: ", chave[0])
            print("Email.....: ", chave[1])
            print("Nome......: ", dado[0]) #nome e nivel estão dentro de usuarios, sendo assim se torna dados de "usuarios"
            print("Nivel.....: ", dado[1])
