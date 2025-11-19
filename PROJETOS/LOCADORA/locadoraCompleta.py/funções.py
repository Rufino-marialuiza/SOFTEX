
import pymysql, os
from dotenv import load_dotenv
load_dotenv()
#criar função de atualizar dados de filmes
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

def cadastrar():
    titulo=input('Titulo do filme a ser cadastrado:').lower()

    try:
        cursor.execute("SELECT * FROM Filmes WHERE titulo = %s", (titulo,))
        existe = cursor.fetchall()

        if existe:
            print('Filme já adicionado!\n')
        else:
            ano_lancamento=int(input("Ano de Lançamento:"))
            genero=input("Gênero:")
            duracao_min=int(input("Duração do filme:"))
            
            dados = (titulo, ano_lancamento, genero, duracao_min)

            cursor.execute("INSERT INTO Filmes (titulo, ano_lancamento, genero, duracao_min) VALUES (%s, %s, %s, %s)", dados)

            novo_id = cursor.lastrowid

            cursor.execute("INSERT INTO disponiveis (titulo, filme_id) VALUES (%s, %s)", (titulo,novo_id))
            conexao.commit()
            print(f"✅ Filme inserido com sucesso! ID Gerado: {novo_id}")

    except pymysql.Error as e:
        print(f"❌ Erro ao cadastrar o filme: {e}")

def remover():
    titulo=input('Titulo do filme a ser removido:').lower()

    try:
        cursor.execute("SELECT * FROM Filmes WHERE titulo = %s", (titulo,))
        existe = cursor.fetchall()

        if existe:
            cursor.execute("DELETE FROM Filmes WHERE titulo = %s", (titulo,))
            cursor.execute("DELETE FROM disponiveis WHERE titulo = %s", (titulo,))
            conexao.commit()
            print('Filme removido de cadastro!\n')

        else:
            opcao=int(input(f'Filme {titulo.capitalize()} não identificado em cadastros. Deseja tentar novamente? (S=1/N=0)'))
            while opcao!=1 and opcao!=0:
                print("❌Resposta inválida, digite novamente")
                opcao=int(input('Filme não identificado em cadastros. Deseja tentar novamente? (S=1/N=0)'))

            if opcao==1:
                remover()

    except pymysql.Error as e:
        print(f"❌ Erro ao remover o filme: {e}")


def disponiveis():
        
    cursor.execute("SELECT titulo, filme_id FROM disponiveis")
    disponiveis = cursor.fetchall()

    if disponiveis:
        print("\n🎬 Lista de Filmes Disponíveis:")
        print("-" * 30)
        for titulo,filme_id in disponiveis:
            print(f"{filme_id} : {titulo.capitalize()}")
        print("-" * 30)

    else:
        opcao=int(input('Nenhum filme cadastrado. cadastrar novos? (S=1/N=0)'))

        while opcao!=1 and opcao!=0:
            print("❌Resposta inválida!")
            opcao=int(input('Nenhum filme cadastrado. cadastrar novos? (S=1/N=0)'))

        if opcao==1:
            cadastrar()
        

def devolucao():
    titulo=input('Titulo do filme:').lower()
    
    cursor.execute("SELECT filme_id, titulo FROM Filmes WHERE titulo = %s", (titulo,))
    existe = cursor.fetchone()

    if existe:
        id = existe[0]

        cursor.execute("INSERT INTO disponiveis (titulo, filme_id) VALUES (%s, %s)", (titulo,id))
        conexao.commit()
        print('✅Filme devolvido!\n')
    else:
        print('❌filme  não havia sido alugado ou não esta cadastrado no sistema!\n')

def alugar():
    titulo=input('Titulo do filme:').lower()

    cursor.execute("SELECT titulo FROM filmes WHERE titulo = %s", (titulo,))
    existe = cursor.fetchone()

    if existe:
        cursor.execute("SELECT titulo FROM disponiveis WHERE titulo = %s", (titulo,))
        disponivel = cursor.fetchall()

        if disponivel:
            cursor.execute("DELETE FROM disponiveis WHERE titulo = %s", (titulo,))
            conexao.commit()
            print('Filme alugado, aproveita e faça a devolução em até 30 dias!\n')

        else:
            opcao=int(input('Filme ja alugado. Escolher outro? (S=1/N=0)'))

            while opcao!=1 and opcao!=0:
                print("❌Resposta inválida!")
                opcao=int(input('Filme ja alugado. Escolher outro? (S=1/N=0)'))

            if opcao==1:
                alugar()

    else:
        print('Filme inexistente no cadastro da locadora!\n')

def fechar():
    cursor.close()
    conexao.close()
    print("Obrigada e até logo :)")