from db_confing import conecatar

def criar_categoria(nome, descricao):
    try:  
        conn = conecatar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categotia (nome, descricao) VALUES (%s, %s) , (nome, descriacao)")
        conn.commit()
        return{"status": "mensagem""categoria criada com sucesso!"}
    except Exception as e:
        return{"status":"erro","mensagem":str(e)}
        conn.close()
        
def listar_categoria():
    try:
        conn = conecatar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categoria")
        return cursor.fetchall()
    except Exception as e:
        return{"status":"erro","mensagem":str(e)}
    finally:
        conn.close()
     

def atualizar_categoria(id_categoria):
    try:
        conn = conecatar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM CATEGORIA WHERE id=&s", (id_categoria,))
                (novo_nome, nova_discricao, id_categoria) )
        conn.commit()
        if cursor.rowcount == 0:
          return{"status":"sucesso","mensagem":"Nenhuma categoria encontrada para atualizar."}
        return{"status":"aviso","mensagem":"categoria atualizar!"}
    except Exception as e:
        conn.close()

def deletar_categoria(id_categoria):
    try:
        conn = conecatar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM CATEGORIA WHERE id=&s", (id_categoria))
        conn.commit()
        if cursor.rowcount == 0:
            return{"status":"aviso","mensagem":"Nenhuma categoria encontrada para deletar."}
        return{"status":"sucesso","mensagem":"categoria excluida"}
    except Exception as e:
        return{"status":"erro","mensagem":str(e)}
    finally:
        conn.close()
      

