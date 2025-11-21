import funçoes
import inquirer

def menu_conta(conta):
    
    while True:
        questions = [
            inquirer.List(
                'opcao',
                message="🏦 Menu do Banco",
                choices=[
                    ('Mostrar Saldo Atual', 0),
                    ('Depositar', 1),
                    ('Saque', 2),
                    ('Apresentar Extrato', 3),
                    ('Sair da Conta', 4)
                ],
                carousel=True
            )
        ]
        
        resposta = inquirer.prompt(questions)
        opcao = resposta['opcao']

        if opcao == 0:
            funçoes.mostrarSaldo(conta)

        elif opcao == 1:
            funçoes.depositar(conta)

        elif opcao == 2:
            funçoes.sacar(conta)

        elif opcao == 3:
            funçoes.extrato(conta)

        elif opcao == 4:
            print("\nSaindo da conta..\n")
            return

def main():

    while True:
        inicio = [
            inquirer.List(
                'entrarNoBanco',
                message="Deseja entrar no banco ou sair?",
                choices=['ENTRAR', 'SAIR'],
            )
        ]
        resposta = inquirer.prompt(inicio)
        
        if resposta['entrarNoBanco'] == 'SAIR':
            funçoes.sair()
            break

        conta = [
            inquirer.List(
                'entrada',
                message="Olá! Você já possui uma conta?",
                choices=[('Sim', 'S'), ('Não', 'N')],
            )
        ]
        resposta = inquirer.prompt(conta)
        
        if resposta['entrada'] == 'S': 
            funçoes.acharUsuario()
        else:
            funçoes.cadastro()

if __name__ == '__main__':
    main()
