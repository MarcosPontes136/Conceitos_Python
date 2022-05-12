#USANDO O WHILE PARA FAZER UMA LISTA
cadastro=[]
resposta="S"
while resposta=="S":
    cadastro.append(input("Paciente: "))
    cadastro.append(int(input("Idade: ")))
    cadastro.append(input("Endereço: "))
    cadastro.append(input("Suspeita de Covid19: "))
    resposta=input("Digite \"S\" para continuar ou \"N\" para sair!\n ").upper()
    # \"S\" é usado para que não entenda somente como texto
    if resposta=="N":
        print("Até Logo!!")

#FORMULA PARA EXIBIR O QUE FOI ESCRITO
for elemento in cadastro:
print(elemento)