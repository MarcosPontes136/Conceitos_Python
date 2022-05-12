pacientes=[]
cpf=[]
idades=[]
enderecos=[]
suspeita_covid=[]
resposta="S"

while resposta== "S":
    pacientes.append(input("Nome do paciente: "))
    cpf.append(int(input("Digite o CPF: ")))
    idades.append(int(input("Idade: ")))
    enderecos.append(input("Endereço: "))
    suspeita_covid.append(input("Paciente tem alguma suspeita de covid19: "))
    resposta=input("Digite \"S\" para continuar ou digite \"N\" para buscar paciente\n") .upper()
    # \"S\" é usado para que não entenda somente como texto
    if resposta== "N":
     busca=input("\nDigite o nome do paciente que deseja buscar: ")

for indice in range(0,len(pacientes)): #for faz aaprecer todo os itens relacionados e solicitados pelo usuario
    if busca==pacientes [indice]:#função if faz com que a busca pelo nome apareça esses itens abaixo.
      print("Paciente...:", pacientes[indice])
      print("CPF........:", cpf[indice])
      print("Endereço...:", enderecos[indice])


