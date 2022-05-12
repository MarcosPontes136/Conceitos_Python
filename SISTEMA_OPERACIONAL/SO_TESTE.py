import platform
import getpass
from datetime import datetime #retorna a data e hora (EUA) da BIOS.

print("Nome maquina............: ", platform.node())
print("Arquitetura.............: ", platform.architecture())
print("Sistema Operacional.....: ", platform.system())
print("Versao do SO............: ", platform.release())
print("Processador.............: ", platform.processor())
print("Versao do Python........:", platform.python_version())




print(datetime.now())

usuario = (getpass.getuser())         #podemos usar o print no lugar de usuario para informar o usuario da marquina
senha = getpass.getpass("Digite sua senha: ") #getpass.getpass deixa invisivel o que esta digitando.
if usuario == "Zeusc" and senha == "Hello":
    print("Bem vindo!")
else:
    print("Você não tem acesso!")