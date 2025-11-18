'''#conectei com o banco de dados do mysql !instalar o PYMYSQL!, ainda tentando criar as tabelas
import pymysql.cursors

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "bolinhodegom4.",
    "database": "locadora",
    "port": 3306
}
conexao = None

try:
    conexao = pymysql.connect(**DB_CONFIG)
    if conexao:
        print("Conexão PyMySQL bem-sucedida ao banco de dados MySQL!")

        comando= """
    CREATE TABLE Filmes (
        filme_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(100) NOT NULL,
        ano_lancamento YEAR,
        genero VARCHAR(50),
        duracao_min INT
    );"""
                
except Exception as e:
    print(f"Erro ao conectar ao MySQL com PyMySQL: {e}")

finally:
    if conexao and conexao.open:
        conexao.close()
        print("Conexão PyMySQL fechada.")'''

import pymysql

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "bolinhodegom4.",
    "database": "locadora",
    "port": 3306
}

try:
    conexao= pymysql.connect(**DB_CONFIG)

    cursor= conexao.cursor()
    cursor.execute("CREATE TABLE Alugados ( filme_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(100) NOT NULL, ano_lancamento YEAR, genero VARCHAR(50),duracao_min INT)")
    conexao.commit()

except pymysql.Error as e:
    print(f"❌ Erro ao conectar ou criar a tabela: {e}")
    
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexao' in locals() and conexao:
        conexao.close()
    print("Conexão e cursor fechados.")   
