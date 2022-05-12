def perguntar():
    return input("O que deseja realizar?\n" +
            "<I> - Para inserir um usuario\n" +
            "<P> - Para pesquisar um usuario\n" +
            "<E> - Excluir usuario\n" +
            "<L> - Listar usuario \n\n").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite sua data de nascimento: "),
                                                   input("Digite a data de acesso: "),
                                                   input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave): #O dicionario(onde se pretende ser pesquisado) e chave( o dado que será pesquisado)
    lista=dicionario.get(chave) #função .get é usado para puxar os dados e verificar se existe a informação
    if lista!=None: # "!=" representa diferente
        print("Nome.............:" + lista[0])
        print("Ultimo acesso....:" + lista[2])
        print("Ultima estação...:" + lista[3])


def excluir(dicionario, chave):
    if dicionario.get(chave):
        del dicionario[chave] #função del usado para deletar um arquivo ou dado.
        print("Objeto eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items(): # items() (Responsavel em retornar em forma de lista os elementos do dicionario)
        print("Objeto......: ")
        print("Usuario.....: ", chave)
        print("Dados.......: ", valor)

