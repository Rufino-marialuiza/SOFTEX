import mysql.connector
#n ta respondendo nada
DB_CONFIG = {
    "host": "localhost",       # Ou o endereço IP/nome do host do seu servidor MySQL
    "user": "hoot",     # Seu nome de usuário do MySQL
    "password": "bolinhodegom4.",   # Sua senha do MySQL
    "database": "locadora", # O nome do banco de dados que você quer usar
    "port": 3306
}

try:
    conexao = mysql.connector.connect(**DB_CONFIG)

    if conexao.is_connected():
        print("Conexão bem-sucedida ao banco de dados MySQL!")

except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão fechada.")