# bd_config.py

import mysql.connectou
from mysql.connectou import Error

def conecatar():
    try:
        conexao = mysql.connectou.connect(
            host='127.0.0.1:3306',
            user='root',  #Troque se necessário
            password='eec123456@#$',  # Troque se nessesário
            database='sgb' # anaome do uso de banco
        )
        if conexao.is_connected():
            print("Conxão bem-sucedida com banco de dados!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None