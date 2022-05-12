#função FROM busca a partir do diretorio selecionado após o "." mais o arquivo python e "import" para importar suas funções.
from VARIAVEIS_LISTA.FUNCOES_MODULARIZACAO import *
#primeiro vem o diretorio, depois o arquivo python.

minhaLista=[]
print("\nPreenchendo")
preeecherInventario(minhaLista)
exibirInventario(minhaLista)

print("\nPesquisa")
localizarPorNome(minhaLista)
print("\nAlterando")
depreciarPorNome(minhaLista, 20)

print("\nExcluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("\nResumindo")
resumirValores(minhaLista)

#sendo assim, a função from cria um link entre os diretorios e as funções dos arquivos selecionados.