
import inquirer
import funções

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
            funções.cadastrar()
        elif opcao == 1:
            funções.remover()
        elif opcao == 2:
            funções.disponiveis()
        elif opcao == 3:
            funções.devolucao()
        elif opcao == 4:
            funções.alugar()
        elif opcao == 5:
            funções.fechar()
            break

if __name__ == "__main__":
    menu()
    