import random
cadastros=[]
agencia=['32', '74', '12']
extratos=[]

def cadastro(nome):
  usuario=[]
  usuario.append(nome)
  escolhaDeAgencia=random.choice(agencia)
  usuario.append(escolhaDeAgencia)
  numerodaconta= len(cadastros)+1
  usuario.append(str(numerodaconta))
  print(f"Cadastro realizado! sua Agencia é: {escolhaDeAgencia} e o número de sua conta é: {numerodaconta}")
  usuario.append('0')
  cadastros.append(usuario.copy())

def acharUsuario(nome, agencia, conta):
  for u in cadastros:
    if u[0]==nome and u[1]==agencia and u[2]==conta:
      return u
  return None

def depositar(usuario,valor):
    usuario[3]=str(float(usuario[3])+valor)
    print("Depósito realizado!")
    extratos.append(f'Depositado ✅: {valor}')

def sacar(usuario, saque):
    while saque>float(usuario[3]) or saque<=0:
        print('Saque inválido, digite um novo valor')
        saque=float(input("Valor do saque:"))
    usuario[3]=str(float(usuario[3])-saque)
    print("Saque realizado!")
    extratos.append(f'Sacado ❌: {saque}')

def extrato():
  print('-'*5, 'EXTRATO','-'*5)
  if len(extratos)==0:
        print("Nenhuma movimentação registrada.")
  else:
    for i in range(len(extratos)):
        print(extratos[i])
    print('-'*19)


cont=1
while cont==1:
  print("-"*7,"BANCO",'-'*7)
  entrarNoBanco=input("Deseja entrar no banco(ENTRAR) ou sair(SAIR):").upper()

  while entrarNoBanco!='SAIR' and entrarNoBanco!='ENTRAR':
    print("Entrada inválida, digite novamente!")
    entrarNoBanco=input("Deseja entrar no banco(ENTRAR) ou sair(SAIR):").upper()

  if entrarNoBanco=='SAIR':
    cont=0
    print("Até logo! 😉")
  
  else:

    entrada= input("Olá! voce já possui uma conta?(S/N)").upper()
    
    while entrada!='S' and entrada!='N':
        print("Entrada não valida, digite novamente S ou N!")
        entrada= input("Olá! voce já possui uma conta?(S/N)").upper()

    if entrada=='S':
      print("~ VALIDAÇÃO ~")
      nome=input("NOME COMPLETO:").upper()
      agencia=input("AGÊNCIA:")
      conta=input("CONTA:")

      usuario=acharUsuario(nome, agencia,conta)

      while usuario is None:
        print("cadastro não encontrado, digite novamente!")
        print("~ VALIDAÇÃO ~")
        nome=input("NOME COMPLETO:").upper()
        agencia=input("AGÊNCIA:")
        conta=input("CONTA:")
      print("Bem vindo(a) de volta!")
    
    else:
      print("~ CADASTRO ~")
      nome=input("NOME COMPLETO:").upper()
      cadastro(nome)
      usuario=cadastros[-1]
      print("Bem vindo(a)!")

    aux=1
    while aux==1:
      print("-"*7,"BANCO",'-'*7)
      print("OPÇÃO 0: MOSTRAR SALDO ATUAL")
      print("OPÇÃO 1: DEPOSITAR")
      print("OPÇÃO 2: SAQUE")
      print("OPÇÃO 3: APRESENTAR EXTRATO")
      print("OPÇÃO 4: SAIR DA CONTA")
      #print("OPÇÃO 5: PAGAMENTO PIX")# a mais
      #print("OPÇÃO 6: EMPRESTIMO/FINANCIAMENTO") # a mais

      opcao=int(input("Sua opção:"))
      
      while 4<opcao and opcao<0:
        print("Opção inválida, digite novamente!")
        opcao=int(input("Sua opção:"))

      if opcao==0:
        print(f"Saldo atual: {usuario[3]}")

      elif opcao==1:
        deposito=float(input("Valor do depósito:"))
        depositar(usuario,deposito)

      elif opcao==2:
        if float(usuario[3])==0:
           print("Saldo insuficiente!")
        else:   
          saque=float(input("Valor do saque:"))
          sacar(usuario,saque)

      elif opcao==3:
        extrato()
      
      elif opcao==4:
        aux=0
        print("Saindo da conta..")
