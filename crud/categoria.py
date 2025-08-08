from db_confing import conecatar

def criar_categoria(nome, descricao):
    conn = conecatar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categotia (nome, descricao) VALUES (%s, %s) , (nome, descriacao)")
    conn.commit()
    conn.close()
    print("Categoria criada com sucesso!")

    def listar_categoria():
        conn = conecatar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categoria")
        categorias = cursor.fetchall()
        conn.close()
        return categorias

def atualizar_categoria(id_categoria, novo_nome, nova_discricao):
    conn = conecatar()
    cursor = conn.cursor()
    cursor.execute("UPDATE categoria SET nome=%s, descricao=%s WHER id=%s",
                    (novo_nome, nova_discricao, id_categoria))
    conn.commit()
    conn.close()
    print("categoria(id_atualizada!")

def deletar_categoria(id_categoria):
    conn = conecatar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM CATEGORIA WHERE id=&s", (id_categoria))
    conn.commit()
    conn.close()
    print("Categoria excluída!")

