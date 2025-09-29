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
