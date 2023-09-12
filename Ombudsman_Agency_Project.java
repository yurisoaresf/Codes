package projetoOuvidoria;

import java.util.ArrayList;
import java.util.List;

public class Menu {
	public static void main(String[] args) {

//Declarando Variáveis//

		String manifestacao = ("");
		String sugestoes = ("");
		String reclamacoes = ("");
		String elogios = ("");

//Menu do Programa//
		while (true) {
			System.out.println("********************************************");
			System.out.println("***   Bem-Vindo a Ouvidoria Unifacisa!   ***");
			System.out.println("********************************************\n");
			System.out.println("1) Enviar uma manifestação");
			System.out.println("2) Listar todas as manifestações");
			System.out.println("3) Listar todas as sugestões");
			System.out.println("4) Listar todas as reclamações");
			System.out.println("5) Listar todos os elogios");
			System.out.println("6) Pesquisar manifestações");
			System.out.println("7) Sair\n");
			System.out.println("********************************************");
			System.out.print("Digite a opção desejada: ");
			int opcao = Teclado.leInt();
			System.out.print("\n");


//Selecionando o tipo de manifestação a se criar.//
			if (opcao == 1) {
				while (true) {
					System.out.println("***   Criar Manifestação!  ***\n");
					System.out.println("Escolha o tipo de manifestação: ");
					System.out.println("1) Sugestão");
					System.out.println("2) Reclamação");
					System.out.println("3) Elogio");
					int tipo = Teclado.leInt();

//Enviando uma manisfetação.//
					if (tipo == 1) {
						System.out.println("Digite sua Sugestão: ");
						sugestoes = Teclado.leString();
						System.out.println("Sugestão criada com sucesso!\n");
						break;

					} else if (tipo == 2) {
						System.out.println("Digite sua Reclamação: ");
						reclamacoes = Teclado.leString();
						System.out.println("Reclamação criada com sucesso!\n");
						break;

					} else if (tipo == 3) {
						System.out.print("Digite seu Elogio: ");
						elogios = Teclado.leString();
						System.out.println("Elogio criado com sucesso!\n");
						break;

					} else {
						System.out.println("Opção Inválida! Digite uma das opções abaixo:\n");
					}
				}
			}

//Exibindo todas as manifestações.//
			else if (opcao == 2) {
				System.out.println("***   Manifestações Existentes:   ***");
				System.out.println("Tipo: Sugestão - " + sugestoes);
				System.out.println("Tipo: Reclamação - " + reclamacoes);
				System.out.println("Tipo: Elogio - " + elogios);
				System.out.print("\n");
				
//Exibindo as sugestoes.//
			} else if (opcao == 3) {
				System.out.println("***   Sugestões Existentes:   ***");
				System.out.println(sugestoes + "\n");
				
//Exibindo as reclamacoes.//
			} else if (opcao == 4) {
				System.out.println("***   Reclamações Existentes:   ***");
				System.out.println(reclamacoes + "\n");
			
//Exibindo os elogios.//	
			} else if (opcao == 5) {
				System.out.println("***   Elogio Existentes:   ***");
				System.out.println(elogios + "\n");
				
//Consultando manifestações.//
			} else if (opcao == 6) {
				System.out.println("Consultar manifestação: ");
				String consulta = Teclado.leString();
				
//Saindo do programa.//
			} else {
				System.out.println("Fim do Programa!");
				break;
			}

		}

	}
}


