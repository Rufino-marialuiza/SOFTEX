import funçoes

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

      usuario=funçoes.acharUsuario(nome, agencia,conta)

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
      funçoes.cadastro(nome)
      usuario=funçoes.cadastros[-1]
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
        funçoes.depositar(usuario,deposito)

      elif opcao==2:
        if float(usuario[3])==0:
           print("Saldo insuficiente!")
        else:   
          saque=float(input("Valor do saque:"))
          funçoes.sacar(usuario,saque)

      elif opcao==3:
        funçoes.extrato()
      
      elif opcao==4:
        aux=0
        print("Saindo da conta..")
