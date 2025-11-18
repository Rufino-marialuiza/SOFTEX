
import inquirer

Listafilmes=[]
alugados=[]

def cadastrar():
    filme=input('Nome do filme:').lower()
    if filme in Listafilmes:
        print('Filme já adicionado!\n')
    else:
        Listafilmes.append(filme)
        print('Filme adicionado!\n')

def remover():
    filme=input('Nome do filme:').lower()
    if filme in Listafilmes:
        Listafilmes.remove(filme)
        print('Filme removido de cadastro!\n')
    else:
        print('nome não identificado em filmes cadastrados!\n')

def disponiveis():

    if Listafilmes==[]:
        opcao=int(input('Nenhum filme cadastrado. cadastrar novos? (S=1/N=0)'))

        while opcao!=1 and opcao!=0:
            print("❌Resposta inválida, digite novamente")
            opcao=int(input('Nenhum filme cadastrado. cadastrar novos? (S=1/N=0)'))

        if opcao==1:
            cadastrar()

    else:
        print('_'*20)
        for i in range(len(Listafilmes)):
            print(f'{i+1}º {Listafilmes[i]}')
        print('_'*20)

def devolucao():
    filme=input('Nome do filme:').lower()

    if filme in alugados:
        Listafilmes.append(filme)
        alugados.remove(filme)
        print('Filme devolvido!\n')
    else:
        print('filme  não havia sido alugado ou não esta cadastrado!\n')

def alugar():
    filme=input('Nome do filme:').lower()
    if filme in alugados:
        opcao=int(input('Filme ja alugado. Escolher outro? (S=1/N=0)'))

        while opcao!=1 and opcao!=0:
            print("❌Resposta inválida, digite novamente")
            opcao=int(input('Filme ja alugado. Escolher outro? (S=1/N=0)'))

        if opcao==1:
            alugar()

    elif filme not in Listafilmes:
        print('Filme inexistente no cadastro da locadora!\n')
    else:
        alugados.append(filme)
        Listafilmes.remove(filme)
        print('Filme alugado, aproveita e faça a devolução em até 30 dias!\n')

def menu():
    while True:
        questions = [
            inquirer.List(
                "opcao",
                message="🎬 Bem-vindo à locadora! Escolha uma opção",
                choices=[
                    ("Cadastrar Filme", 0),
                    ("Remover Cadastro de filme",1),
                    ("Mostrar Disponíveis", 2),
                    ("Devolver um Filme", 3),
                    ("Alugar", 4),
                    ("Sair", 5),
                ],
            )
        ]
        resposta = inquirer.prompt(questions)

        opcao = resposta["opcao"]

        if opcao == 0:
            cadastrar()
        elif opcao == 1:
            remover()
        elif opcao == 2:
            disponiveis()
        elif opcao == 3:
            devolucao()
        elif opcao == 4:
            alugar()
        elif opcao == 5:
            print("Obrigada e até logo :)")
            break

if __name__ == "__main__":
    menu()
    