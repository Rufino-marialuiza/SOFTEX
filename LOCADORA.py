
import inquirer

Listafilmes=[]
alugados=[]

def cadastrar():
    filme=input('Nome do filme:').lower()
    if filme in Listafilmes:
        print('Filme já adicionado!')
    else:
        Listafilmes.append(filme)
        print('Filme adicionado!')

def disponiveis():

    if Listafilmes==[]:
        opcao=int(input('Nenhum filme cadastrado. cadastrar novos? (S=1/N=0)'))
        if opcao==1:
            cadastrar(opcao)

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
        print('Filme devolvido!')
    else:
        print('filme  não havia sido alugado ou não esta cadastrado!')

def alugar():
    filme=input('Nome do filme:').lower()
    if filme in alugados:
        opcao=int(input('Filme ja alugado. Escolher outro? (S=1/N=0)'))
        if opcao==1:
            alugar(opcao)

    elif filme not in Listafilmes:
        print('Filme inexistente no cadastro da locadora!')
    else:
        alugados.append(filme)
        Listafilmes.remove(filme)
        print('Filme alugado, aproveita e faça a devolução em até 30 dias!')

def menu():
    while True:
        questions = [
            inquirer.List(
                "opcao",
                message="🎬 Bem-vindo à locadora! Escolha uma opção",
                choices=[
                    ("Cadastrar Filme", 0),
                    ("Mostrar Disponíveis", 1),
                    ("Devolver um Filme", 2),
                    ("Alugar", 3),
                    ("Sair", 4),
                ],
            )
        ]
        resposta = inquirer.prompt(questions)

        opcao = resposta["opcao"]

        if opcao == 0:
            cadastrar()
        elif opcao == 1:
            disponiveis()
        elif opcao == 2:
            devolucao()
        elif opcao == 3:
            alugar()
        elif opcao == 4:
            print("Obrigada e até logo :)")
            break

if __name__ == "__main__":
    menu()