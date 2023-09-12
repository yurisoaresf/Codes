from opearacoesbd import *
conn = abrirBancoDados('localhost','root','qualquercoisa','ouvidoria')

opcao = 0
tipos = ['Sugestão', 'Reclamação', 'Elogio']

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
        sql = "SELECT * FROM ouvidoria"
        resultado = listarBancoDados(conn, sql)

        for elemento in resultado:
            print('ID: {0}, Nome: {1}, Tipo: {2}, Descricao: {3}'.format(*elemento))

    elif opcao == 2:
        sql = "SELECT * FROM ouvidoria WHERE tipo = 'Sugestão'"
        resultado = listarBancoDados(conn, sql)

        for elemento in resultado:
            print('ID: {0}, Nome: {1}, Tipo: {2}, Descricao: {3}'.format(*elemento))

    elif opcao == 3:
        sql = "SELECT * FROM ouvidoria WHERE tipo = 'Reclamação'"
        resultado = listarBancoDados(conn, sql)

        for elemento in resultado:
            print('ID: {0}, Nome: {1}, Tipo: {2}, Descricao: {3}'.format(*elemento))

    elif opcao == 4:
        sql = "SELECT * FROM ouvidoria WHERE tipo = 'Elogio'"
        resultado = listarBancoDados(conn, sql)

        for elemento in resultado:
            print('ID: {0}, Nome: {1}, Tipo: {2}, Descricao: {3}'.format(*elemento))

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
        tipo = tipos[tipoEscolhido - 1]

        descricao = input('Digite a descrição: ')
        print()
        print('Manifesto criado com sucesso!')
        print()

        sql = "INSERT INTO ouvidoria (nome,tipo,descricao) VALUES (%s, %s, %s)"
        dados = (nome, tipo, descricao)
        insertNoBancoDados(conn, sql, dados)

    elif opcao == 6:
        pesquisa = int(input('Digite seu número de protocolo(ID): '))

        sql = "SELECT * FROM ouvidoria WHERE id = {0}".format(pesquisa)
        resultado = listarBancoDados(conn, sql)

        for elemento in resultado:
            print('ID: {0}, Nome: {1}, Tipo: {2}, Descricao: {3}'.format(*elemento))


encerrarBancoDados(conn)

print('Fim do programa!')
