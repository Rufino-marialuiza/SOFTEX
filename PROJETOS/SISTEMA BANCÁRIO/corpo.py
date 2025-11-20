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
                carousel=True # Ajuda na navegação, como
            )
        ]
        
        resposta = inquirer.prompt(questions)
            
        opcao = resposta['opcao']

        if opcao == 0:
            # Assumindo que o saldo está na posição 3 de 'usuario'
            print(f"\n💵 Saldo atual: R$ {usuario[3]:.2f}\n") 

        elif opcao == 1:
            deposito_q = [inquirer.Text('deposito', message="💰 Valor do depósito")]
            deposito_a = inquirer.prompt(deposito_q)
            if deposito_a:
                try:
                    deposito = float(deposito_a['deposito'])
                    funçoes.depositar(usuario, deposito)
                except ValueError:
                    print("\n❌ Valor inválido. Tente novamente.\n")

        elif opcao == 2:
            # Verifica se o saldo é zero antes de pedir o valor do saque
            if float(usuario[3]) == 0:
                print("\n❌ Saldo insuficiente!\n")
            else:
                saque_q = [inquirer.Text('saque', message="💸 Valor do saque")]
                saque_a = inquirer.prompt(saque_q)
                if saque_a:
                    try:
                        saque = float(saque_a['saque'])
                        funçoes.sacar(usuario, saque)
                    except ValueError:
                        print("\n❌ Valor inválido. Tente novamente.\n")

        elif opcao == 3:
            print("\n📜 Extrato:\n")
            funçoes.extrato()
            print("\n")

        elif opcao == 4:
            print("\n👋 Saindo da conta..\n")
            return # Sai do loop e retorna para o menu principal

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
