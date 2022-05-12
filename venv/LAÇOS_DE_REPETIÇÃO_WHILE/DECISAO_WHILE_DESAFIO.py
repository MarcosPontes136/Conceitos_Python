nome=input("Nome do Paciente: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa: ") .upper()

while doenca_infectocontagiosa !="SIM" and doenca_infectocontagiosa !="NAO":
    print("Digite SIM ou NAO")
    doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa: ") .upper()

if doenca_infectocontagiosa=="SIM":
    print("Encaminhar paciente para a sala AMARELA")
else:
    print("Encaminhar paciente para a sal BRANCA")

if idade>=65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ") .upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está gravida? ") .upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")