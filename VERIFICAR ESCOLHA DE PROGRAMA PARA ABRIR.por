//Verificar escolha para abertura de programa

programa
{
	
	funcao inicio()
	{
		escreva("\n1 - Abrir Netflix \n2 - Abrir Amazon Prime \n3 - Abrir HBO Go \n4 - Sair")
		inteiro menu = 0

		escreva("\nSua opção")
		leia(menu)
		escolha (menu)
		{

		caso 1:                      //testando se o valor é igual a 1 
		escreva("OK!! Abrir Netflix")
		pare
	
		
		caso 2:                     //testando se o valor é igual a 2
		escreva("OK!! Abrindo Amazon Prime")
		pare
			
		
		caso 3:                     //testando se o valor é igual a 3
		escreva("Ok!! Vamos abrir HBO GO")
		pare
			
		
		caso 4:                    //testando se o valor é igual a 4
		escreva("É uma ordem, saindo!")
		pare

		caso contrario:
		escreva("Você deve escolher as opções 1, 2, 3 ou 4")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 59; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */