import mysql.connector
#n ta respondendo nada
DB_CONFIG = {
    "host": "localhost",       
    "user": "hoot",     
    "password": "bolinhodegom4.",   
    "database": "locadora",
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