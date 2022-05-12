#NESSE CODIGO USAMOS O DEF PARA CRIAR ESTRUTURAS/DEFINIR FUNÇÕES E PARA GERAR UM CODIGO MAIS LIMPO!

def preeecherInventario(lista):
    resposta="S"
    while resposta == "S":
        equipamento = [input("Equipamento: "),
                       int(input("Valor: ")),
                       float(input("Serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resposta = input("Digite \"S\" para continuar: ").upper()
#laço terminado
def exibiIrnventario(lista):
    for elemento in lista:
        print("\nNome...........:", elemento[0])
        print("Valor..........:", elemento[1])
        print("Serial.........:", elemento[2])
        print("Departamento...:", elemento[3])
#
def localizarPorNome(lista):
    busca = input("\nDigite o equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Nome.......:", elemento[0])
            print("Valor......:", elemento[1])
            print("Serial.....:", elemento[2])
#
def depreciarPorNome(lista, porc):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo......:", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("Novo valor: ", elemento[1])
#
def excluirPorSerial(lista):
    serial = int(input("Digite o serial a ser excluido: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    for elemento in lista:
       print("Nome...........:", elemento[0])
       print("Valor..........:", elemento[1])
       print("Serial.........:", elemento[2])
       print("Departamento...:", elemento[3])
#
def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))

