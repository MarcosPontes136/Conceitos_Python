//FUNÇÃO DO ALGORITMO: CALCULAR A MÉDIA ARITMÉDICA

programa
{
	
	funcao inicio()
	{
		real janeiro,fevereiro,marco,abril,media,soma,comentario
		cadeia Venda

		escreva("Digite o valor de venda do mês representado:\nJaneiro:")
		leia(janeiro)
		escreva("Fevereiro:")
		leia(fevereiro)
		escreva("Março:")
		leia(marco)
		escreva("Abril:")
		leia(abril)

		soma = (janeiro+fevereiro+marco+abril)
		media = (janeiro+fevereiro+marco+abril)/4
		//CALCULO DA MEDIA E SOMA

		escreva("Valor total: " + soma + "\nObteve em média: " + media)
		//APLICAÇÃO DOS VALORES ARITMEDICO
		 se (media>=5000.0) {
		 	escreva
		 	("\nOs lucros foram atingidos, MUITO BOM!!")
	          }
	          
	      senao {
	      	escreva("\nInfelismente não atigiu o esperado")
	      }
	      
	      escreva("\nNesse caso, gostaria de anotar algum comentario?\n")
	      leia(comentario)
	    
	}
	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 870; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */