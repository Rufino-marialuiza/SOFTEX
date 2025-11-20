import random, pymysql, os, corpo
from dotenv import load_dotenv
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"), #criar os arquivos gitignore e .ven
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
    "port": int(os.getenv("DB_PORT", 3306))
}

conexao = None
cursor = None

conexao= pymysql.connect(**DB_CONFIG)
cursor= conexao.cursor()

cadastros=[]
agencia=['32', '74', '12']
extratos=[]

def mostrarSaldo():
   
   cursor.execute("SELECT FROM cadastros WHERE nome = %s", (nome,)) #variavel nome

def cadastro():

    nome=input("Nome completo:")
    escolhaDeAgencia=random.choice(agencia)
    saldo=0

    cursor.execute("INSERT INTO sisbancario(nome, agencia, saldo) VALUES (%s,%s,%s)",(nome,escolhaDeAgencia,saldo))
    
    print(f"🎉 Bem vindo(a), {nome}! sua Agencia é: {escolhaDeAgencia} e o número de sua conta é: {cursor.lastrowid}")
    corpo.menu_conta(cursor.lastrowid)

def acharUsuario():
    
    print("\n~ VALIDAÇÃO ~")
    nome=input("Seu nome:")
    agencia=int(input("Digite sua agencia:"))
    conta=int(input("numero da conta"))

    cursor.execute("SELECT * FROM sisbancario WHERE nome = %s agencia = %s conta = %s", (nome,agencia, conta)) #verif. se isso ta certo
    cadastrado= cursor.fetchone()

    if cadastrado:
      print("\n👋 Bem vindo(a) de volta!\n")
      corpo.menu_conta(conta)

    else:
      escolha=input("\n❌ Cadastro não encontrado! tentar novamente?(S/N)").upper()

      while escolha!= 'S' and escolha!='N':
         print("Digite novamente!")
         escolha=input("\n❌ Cadastro não encontrado! tentar novamente?(S/N)").upper()

      if escolha == 'S':
         acharUsuario()

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

def sair():
   cursor.close()
   conexao.close()
   print("Até logo! 😉")