//DEMOSTRATIVO DE MATRIZ E VETOR POR OUTROS MEIOS

programa
{
	
	funcao inicio()
	{
		inteiro contador=0
		cadeia contato[][]={{"João","São Paulo","(11)-9999-5241"},{"Maria","Ribeirão Preto","(11)-9999-8596"},{"Ana","Manaus","(92)-9999-8574"}}

		faca{           //DEMOSTRATIVO DE MATRIZ E VETOR 
			escreva ("Nome:" + contato[contador][0] + "\nCidade:" + contato[contador][1] + "\nContato:" + contato[contador][2] + "\n")
			contador++
			
		}enquanto (contador<=2)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */