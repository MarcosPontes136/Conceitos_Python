pacientes=[]
idades=[]
enderecos=[]
suspeita_covid=[]
resposta="S"

while resposta== "S":
    pacientes.append(input("Nome do paciente: "))
    idades.append(int(input("Idade: ")))
    enderecos.append(input("Endereço: "))
    suspeita_covid.append(input("Paciente tem alguma suspeita de covid19: "))
    resposta=input("Digite \"S\" para continuar ou digite \"N\" para sair\n") .upper()
    # \"S\" é usado para que não entenda somente como texto
    if resposta== "N":
        print("Até logo!!")

        for indice in range (0,len(pacientes)):
            print("\nPaciente...:", pacientes[indice])
            print("Idade......:", idades[indice])
            print("Endereço...:", enderecos[indice])
            print("Com covid..:", suspeita_covid[indice])


