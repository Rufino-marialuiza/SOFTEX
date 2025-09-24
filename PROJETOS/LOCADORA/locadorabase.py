Listafilmes=[]
alugados=[]

cont=1

while cont==1:
    print('-'*30)
    print('BEM VINDO A LOCADORA')
    print('OPÇÃO: 0 CADASTRAR FILMES')
    print('OPÇÃO: 1 MOSTRAR DISPONIVEIS')
    print('OPÇÃO: 2 DEVOLVER UM FILME')
    print('OPÇÃO: 3 ALUGAR')
    print('OPÇÃO: 4 SAIR')
    print('-'*30)

    opcao=int(input('OPÇÃO:'))

    if opcao==0:
        filme=input('Nome do filme:').lower()
        if filme in Listafilmes:
            print('Filme já adicionado!')
        else:
            Listafilmes.append(filme)
            print('Filme adicionado!')

    elif opcao==1:
        if Listafilmes==[]:
            opcao=int(input('Nenhum filme cadastrado. cadastrar novos? (S=1/N=0)'))
            if opcao==1:
                filme=input('Nome do filme:').lower()
                if filme in Listafilmes:
                    print('Filme já adicionado!')
                else:
                    Listafilmes.append(filme)
                    print('Filme adicionado!')

        else:
            print('_'*20)
            for i in range(len(Listafilmes)):
                print(f'{i+1}º {Listafilmes[i]}')
            print('_'*20)

    elif opcao==2:
        filme=input('Nome do filme:').lower()

        if filme in alugados:
            Listafilmes.append(filme)
            alugados.remove(filme)
            print('Filme devolvido!')
        else:
            print('filme  não havia sido alugado ou não esta cadastrado!')

    elif opcao==3:
        filme=input('Nome do filme:').lower()
        if filme in alugados:
            print('Filme ja alugado')

        elif filme not in Listafilmes:
            print('Filme inexistente no cadastro da locadora!')
        else:
            alugados.append(filme)
            Listafilmes.remove(filme)
            print('Filme alugado, aproveita e faça a devolução em até 30 dias!')

    elif opcao==4:
        cont=0

    else:
        print('Opção inválida!')


print('Obrigada e ate logo :)')
