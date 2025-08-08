# app.py

from db_confing import conecatar
from crud import categoria

from db_config import conectar

def main():
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM livros;") # Exemplo de consulta simples 

            resultados = cursor.fetchall()

            print("\nLivros cadastrados:")
            for linha in resultados:
                print(linha)

        except Exception as e:
            print(f"Erro na execução: {e}")
        finally:
            conexao.close()
            print("\nConexão encerrada.")

if __name__ == "__main__":
    main()

def manu():
    while True:
        print("\n=== MENU SGB ===")
        print("1. Criar categori")
        print("2. listar categoria")
        print("3. Atualizar Categoria")
        print("4. Delete Categoria")
        print("0. Sair")
        print = input("Escolar uma opção: ")

if open == "1":
    nome = input("Nome da categoria:")
    descriacao = input ("Descri")

        
    
   