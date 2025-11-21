import random, pymysql, os, corpo
from dotenv import load_dotenv
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
    "port": int(os.getenv("DB_PORT", 3306))
}

conexao = None
cursor = None

conexao= pymysql.connect(**DB_CONFIG)
cursor= conexao.cursor()

agencia=['32', '74', '12']
extratos=[]

def cadastro():

    nome=input("Nome completo:").lower()
    escolhaDeAgencia=random.choice(agencia)
    saldo=0.00

    cursor.execute("INSERT INTO cadastros (nome, agencia, saldo) VALUES (%s,%s,%s)",(nome,escolhaDeAgencia,saldo))
    conexao.commit()
    
    print(f"🎉 Bem vindo(a), {nome}! sua Agencia é: {escolhaDeAgencia} e o número de sua conta é: {cursor.lastrowid}")
    corpo.menu_conta(cursor.lastrowid)

def acharUsuario():
    
    print("\n~ VALIDAÇÃO ~")
    nome=input("Seu nome:").lower()
    agencia=int(input("Digite sua agencia:"))
    conta=int(input("numero da conta"))

    cursor.execute("SELECT * FROM cadastros WHERE nome = %s AND agencia = %s AND conta = %s", (nome,agencia, conta))
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

def mostrarSaldo(conta):
   
   cursor.execute("SELECT saldo FROM cadastros WHERE conta = %s", (conta,))
   saldo= cursor.fetchone()[0]
   print(f"💵 Saldo atual: R$ {saldo:.2f}")

def depositar(conta):

    deposito= float(input("💰 Valor do depósito:"))

    while deposito<=0:
       print("❌ O valor do depósito deve ser positivo, digite novamente.")
       deposito= float(input("💰 Valor do depósito:"))

    cursor.execute("UPDATE cadastros SET saldo = saldo + %s WHERE conta = %s", (deposito,conta))
    conexao.commit()

    print("Depósito realizado!")
    
    cursor.execute("INSERT INTO extratos(conta, tipo, valor, data_hora) VALUES(%s,%s,%s, NOW())",(conta,'DEPÓSITO',deposito))
    conexao.commit()

def sacar(conta):

    cursor.execute("SELECT saldo FROM cadastros WHERE conta = %s", (conta,))
    saldo= cursor.fetchone()[0]

    if saldo==0.00:
       print("❌ Saldo insuficiente!")

    else:
        saque=float(input("💸 Valor do saque:"))

        while saque>saldo or saque<=0:
            print('Saque inválido, digite um novo valor')
            saque=float(input("💸 Valor do saque:"))

        cursor.execute("UPDATE cadastros SET saldo = saldo - %s WHERE conta = %s", (saque,conta))
        conexao.commit()

        print("Saque realizado!")

        cursor.execute("INSERT INTO extratos(conta, tipo, valor, data_hora) VALUES(%s,%s,%s, NOW())",(conta,'SAQUE',saque))
        conexao.commit()

def extrato(conta): 

    print('-'*5, 'EXTRATO','-'*5)

    cursor.execute("SELECT tipo, valor, DATE_FORMAT(data_hora, '%%d/%%m/%%Y %%H:%%i') AS data_formatada FROM extratos WHERE conta = %s ORDER BY data_hora DESC",(conta))
    movimentacoes= cursor.fetchall()

    if movimentacoes== None:
        print("Nenhuma movimentação registrada.")

    else:
        for tipo,valor,data in movimentacoes:
            simbolo = '✅' if tipo == 'DEPÓSITO' else '❌'
            print(f"[{data}] {tipo} {simbolo}: R$ {valor}")

    print('-'*19)

def sair():
   cursor.close()
   conexao.close()
   print("Até logo! 😉")