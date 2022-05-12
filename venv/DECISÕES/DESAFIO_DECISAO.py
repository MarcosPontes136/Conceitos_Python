nome=input("Digite o nível de acesso: ") .upper()
if niver=="ADM" or niver=="USR":
    genero=input("Digie seu gênero:") .upper()
if nivel=="ADM":
    if genero=="FEMININO":
     print("Olá Administradora")
    else:
     print("Olá Administrador")
    else:
        print("Olá usuario")
    else:
        print("Olá usuaria")
    elif nivel=="GUEST":
    print("Olá visitante")
    else:
    print("Ola desconhecido(a)")