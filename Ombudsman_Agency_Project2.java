package ouvidoriafacisa;

import java.util.ArrayList;

public class OuvidoriaUnifacisa {
	public static void main(String[] args) {

		ArrayList<Teste> listaManifestacoes = new ArrayList<>();
		ArrayList<Teste> listaSugestao = new ArrayList<>();
		ArrayList<Teste> listaReclamacao = new ArrayList<>();
		ArrayList<Teste> listaElogio = new ArrayList<>();

		while (true) {
			System.out.println("Bem vindo a Ouvidoria Unifacisa!\n");
			System.out.println("1) Criar Manifestação");
			System.out.println("2) Listar Manifestações");
			System.out.println("3) Listar Sugestões");
			System.out.println("4) Listar Reclamações");
			System.out.println("5) Listar Elogios");
			System.out.println("6) Pesquisar Manifestação pelo ID");
			System.out.println("7) Sair\n");
			System.out.println("Digite sua opção: ");
			int opcao = Teclado.leInt();

			if (opcao == 1) {
				while (true) {
					System.out.println("Escolha o tipo de Manifestação: ");
					System.out.println("1) Sugestão");
					System.out.println("2) Reclamação");
					System.out.println("3) Elogio");
					int tipo = Teclado.leInt();

					if (tipo == 1) {
						Teste novaSugestao = new Teste();
						System.out.println("Digite seu nome: ");
						novaSugestao.nome = Teclado.leString();
						System.out.println("Descreva sua Sugestão: ");
						novaSugestao.descricao = Teclado.leString();
						System.out.println("Sugestao registrada com sucesso!\n");
						listaSugestao.add(novaSugestao);
						listaManifestacoes.add(novaSugestao);
						break;

					} else if (tipo == 2) {
						Teste novaReclamacao = new Teste();
						System.out.println("Descreva sua Reclamação: ");
						novaReclamacao.descricao = Teclado.leString();
						System.out.println("Reclamação registrada com sucesso!\n");
						listaReclamacao.add(novaReclamacao);
						listaManifestacoes.add(novaReclamacao);
						break;

					} else if (tipo == 3) {
						Teste novoElogio = new Teste();
						System.out.println("Descreva sua Elogio: ");
						novoElogio.descricao = Teclado.leString();
						System.out.println("Elogio registrado com sucesso!\n");
						listaReclamacao.add(novoElogio);
						listaManifestacoes.add(novoElogio);
						break;

					} else {
						System.out.println("Opcão inválida, tenta novamente :D");
					}
				}
			}
			if (opcao == 2) {
				int indice = 0;
				System.out.println("Manifestações Existentes:");
				for (Teste m : listaManifestacoes) {
					indice++;
					System.out.println(
							"ID: " + indice + " - " + "Requerente: " + m.nome + " - Descrição: " + m.descricao);
				}
			} else if (opcao == 3) {
				int indice = 0;
				System.out.println("Sugestões realizadas: ");
				for (Teste s : listaSugestao) {
					indice++;
					System.out.println("ID: " + indice + " - Descrição: " + s.descricao);
				}
			} else if (opcao == 4) {
				int indice = 0;
				System.out.println("Reclamações realizadas: ");
				for (Teste r : listaReclamacao) {
					indice++;
					System.out.println("ID: " + indice + " - Descrição: " + r.descricao);
				}
			} else if (opcao == 5) {
				int indice = 0;
				System.out.println("Elogios realizados: ");
				for (Teste e : listaElogio) {
					indice++;
					System.out.println("ID: " + indice + " - Descrição: " + e.descricao);
				}
			} else if (opcao == 6) {
				System.out.println("Digite o ID da manifestação: ");
				int indice = Teclado.leInt() - 1;
				Teste i = listaManifestacoes.get(indice);
				System.out.println("Requerente: " + i.nome + " - " + i.descricao);

			} else if (opcao == 7) {
				System.out.println("Fim do programa!");
				break;
			} else {
			}
		}
	}
}
