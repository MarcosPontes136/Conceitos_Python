nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ") .upper()
if doenca_infectocontagiosa=="SIM":
    print("Encaminhar o paciente para sala AMARELA")
elif doenca_infectocontagiosa=="NAO":
     print("Encaminhar o paciente para sala BRANCA")
else:
     print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

# PROBLEMA SOLUCIONADO EM RELAÇÃO A GRAVIDEZ E SUAS PRIORIDADES
if idade >= 65:
    print("Paciente COM prioridade!")
else:
 genero =input("Digite o gênero do paciente: ") .upper()
 if genero=="FEMININO" and idade >10:
    gravidez=input("A paciente está gravida? ") . upper()
    if gravidez=="SIM":
     print("Paciente COM prioridade")
    else:
         print("Paciente SEM prioridade")