import psycopg2
from dotenv import load_dotenv
import os

def conectar():
    load_dotenv()

    host = os.getenv('DB_HOST')
    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    port = os.getenv('DB_PORT')

    conexao = psycopg2.connect(
        host= host,
        dbname= dbname,
        user= user,
        password= password,
        port= port,

    )
    return conexao


if __name__ == '__main__':
    conexao = conectar()
    print("Conectado com sucesso!")
    conexao.close()