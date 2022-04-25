opcao = 0
tipos = ['Sugestão', 'Reclamação', 'Elogio']
manifestacoes = []
sugestoes = []
reclamacoes = []
elogios = []

while opcao != 7:

    print('Bem vindo a Ouvidoria Unifacisa')
    print()
    print('1) Listar todas as manifestações')
    print('2) Listar todas as sugestões')
    print('3) Listar todas as reclamações')
    print('4) Listar todos os elogios')
    print('5) Enviar uma manifestação')
    print('6) Pesquisar protocolo por número ID')
    print('7) Sair')

    print()
    opcao = int(input('Qual opção você deseja continuar: '))
    print()

    if opcao < 1 or opcao > 7:
        print('Entrada inválida. Favor digitar uma das opções abaixo!')
        print()

    if opcao == 1:
        print('Todas as manifestações encontradas:')
        print()
        for manifestacaoTodas in manifestacoes:
            estaManifestacao = manifestacaoTodas.split(' # ')
            print(estaManifestacao[0] + ' - ' + estaManifestacao[1] + ' - ' + estaManifestacao[2] + ' - ' +
                  estaManifestacao[3])

    elif opcao == 2:
        print('Todas as sugestões encontradas:')
        print()
        for sugestoesTodas in sugestoes:
            estaManifestacao = sugestoesTodas.split(' # ')
            print(estaManifestacao[0] + ' - ' + estaManifestacao[1] + ' - ' + estaManifestacao[2])

    elif opcao == 3:
        print('Todas as reclamações encontradas:')
        print()
        for reclamacoesTodas in reclamacoes:
            estaManifestacao = reclamacoesTodas.split(' # ')
            print(estaManifestacao[0] + ' - ' + estaManifestacao[1] + ' - ' + estaManifestacao[2])

    elif opcao == 4:
        print('Todos os elogios encontrados:')
        print()
        for elogiosTodos in elogios:
            estaManifestacao = elogiosTodos.split(' # ')
            print(estaManifestacao[0] + ' - ' + estaManifestacao[1] + ' - ' + estaManifestacao[2])

    elif opcao == 5:
        nome = input('Digite seu nome: ')
        print()
        print('Tipo de manifestação:')
        print()
        quantidadeTipos = len(tipos)

        for t in range(quantidadeTipos):
            print(t + 1, ')', tipos[t])
            print()

        tipoEscolhido = int(input('Digite sua opção: '))
        print()
        descricao = input('Digite a descrição: ')
        print()
        print('Manifesto criado com sucesso!')
        print()

        # adicionando Manifestacoes a lista de manifestacoes:
        codigo = str(len(manifestacoes) + 1)
        tipo = tipos[tipoEscolhido - 1]
        manifestoGeral = 'Código ' + codigo + ' # ' + 'Tipo ' + tipo + ' # ' + 'Requisitante: ' + nome + ' # ' + descricao
        manifestacoes.append(manifestoGeral)

        if tipoEscolhido == 1:
            # adicionando Sugestão a lista de sugestão:
            codigo = str(len(sugestoes) + 1)
            manifesto = 'Código ' + codigo + ' # ' + 'Requisitante: ' + nome + ' # ' + descricao
            sugestoes.append(manifesto)

        elif tipoEscolhido == 2:
            # adicionando Reclamação a lista de reclamações:
            codigo = str(len(reclamacoes) + 1)
            manifesto = 'Código ' + codigo + ' # ' + 'Requisitante: ' + nome + ' # ' + descricao
            reclamacoes.append(manifesto)

        elif tipoEscolhido == 3:
            # adicionando Elogio a lista de elogios:
            codigo = str(len(elogios) + 1)
            manifesto = 'Código ' + codigo + ' # ' + 'Requisitante: ' + nome + ' # ' + descricao
            elogios.append(manifesto)

    elif opcao == 6:
        pesquisa = int(input('Digite seu número de protocolo(ID): '))
        protocolo = manifestacoes[pesquisa - 1].split(' # ')
        print(protocolo[0])
        print(protocolo[1])
        print(protocolo[2])
        print(protocolo[3])

print('Fim do programa!')