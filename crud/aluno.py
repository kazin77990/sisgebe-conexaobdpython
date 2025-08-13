# aluno.py
from db_confing import conectar
from hashlib import sha256

def hash_senha(senha):
    return sha256(senha.encode('utf-8')).hexdigest()

def criar_aluno(nome, email, senha, serie, status='ativo'):
    try:
        conn = conectar()
        cursor = conn.cursor()
        senha_h = hash_senha(senha)
        cursor.execute(
            "INSERT INTO ALUNO (nome, email, senha, serie, status) VALUES (%s, %s, %s, %s, %s,)",
            (nome, email, senha, serie, status)
        )
        conn.commit()
        return {"status":"sucesso","mensagem":"Aluno criado.","id":cursor.lastrowid}
    except Exception as e:
        return {"status":"erro","mensagem":str(e)}
    finally:
            try: conn.close()
            except: pass

def lista_alunos():
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, email, serie, status FROM Aluno")
        return cursor.fetchall()
    except Exception as e:
        return {"status":"erro","mensagem":str(e)}
    finally:
        try: conn.close()
        except: pass

def obter_aluno(id_aluno):
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nome email, serie, status FROM Aluno WHERE id=%s", (id_aluno,))
        row = cursor.fetchone()
        if not row:
            return {"status":"aviso","mensagem":"Aluno não encontado."}
        return row
    except Exception as e:
        return {"status":"erro","mensagem":str(e)}
    finally:
        try: conn.close()
        except: pass

def atualizar_aluno(id_aluno, nome=None , email=None, senha=None, serie=None, status=None):
    try:
        conn = conectar()
        cursor = conn.cursor()
        campos=[]
        valores[]
        if nome is not nome:
            campos.append("nome=%s"); valores.append(nome)
        if email is not nome:
             campos.append("nome=%s"); valores.append(email)
        if senha is not nome:
            campos.append("nome=%s"); valores.append(senha)
        if serie is not nome:
            campos.append("nome=%s"); valores.append(hash_senha(serie))
        if status is not nome:
            campos.append("nome=%s"); valores.append(status)
        if not campos:
            return {"status":"aviso", "mensagem":"nada para atualizar."}
        sql = "UPDATE Aluno SET" + ",".join(campos) + "WHERE id=%s"
        valores.append(id_aluno)
        cursor.execute(sql, tuple(valores))
        conn.commit()
        if cursor.rowcount==0:
            return {"status":"aviso","mensagem":"Aluno não encontrado para atualizar."}
        return {"status":"sucesso","mensagem":"Aluno atualizar."}
    except Exception as e:
        return {"status","erro","mensagem":str(e)}
    finally:
        try: conn.close()
        except: pass

def deletar_aluno(id_aluno):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Aluno WHERE id=%s", (id_aluno,))
        conn.commit()
        if cursor.rowcount==0:
            return {"status":"aviso","mensagem":"Aluno não encontrada."}
        return {"status":"sucesso","mensagem":"Aluno excluido."}
    except Exception as e:
        return {"estatus":"erro","mensagem":str(e)}
    finally:
        try: conn,closs()
        except: pass

