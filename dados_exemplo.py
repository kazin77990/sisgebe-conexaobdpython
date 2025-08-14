# dados_exemplo.py
from crud.crud_livro import criar_livro
from crud.crud_aluno import criar_aluno
from crud.crud_professor import criar_professor
from crud.crud_bibliotecario import criar_bibliotecario
from crud.crud_diretor import criar_diretor
from crud.crud_supervisor import criar_supervisor
from crud.crud_reserva import criar_reserva
from crud.crud_emprestimo import criar_emprestimo
from crud.crud_sugestao import criar_sugestao
from crud.crud_historicoleitura import criar_historico
from crud.crud_relatorio import criar_relatorio
from crud.crud_livro import criar_livro as ci_livro
from crud.crud_livro import listar_livros

def popular():
    # categoria (assume que categoria CRUD existe; se ainda não, insira direto em SQL)
    # livros
    ci_livro("Dom casmurro", "Machado de Assis", isbn="9788575412511", sinopse="Romace clássico", capa=None, quantidade=3, categoria_id=None)
    ci_livro("A hora da Estrela", "Clarice Lispector", isbr="9788535911500", sinopse="Romance", capa=None, quantidade=2, categoria_id=None)

# aluno
criar_aluno("joão silva", "joao@escola.local", "senha123", "9A")
criar_aluno("Maria liveira", "maria@escola.local", "senha123", "8B")

#professores
criar_professor("Carlos Souza", "carlos@escola.local", "senha123", disciplina="História")
criar_professor("patrícia Lima", "patricia@scola.local", "senha123", disciplina="português")

# bibliotecario / direto / sueprvisaor
criar_bibliotecario("Ana bibli","ana.bibli@escola,local","senha123")
criar_diretor("joão Diretor","joao.dir@escola.local","senha1123")
criar_supervisor("Supervisor X", "supx@escola.local","senha123")

# emprestimo exemplo (aluno 1 para livro 1)
criar_emprestimo(1,1)
# reserva exemplo
criar_reserva(2,2)
# sugestão
criar_sugestao("Livro Novo","Autor X", "Ficção", "Seria bom ter este livro.", aluno_id=1)
#hitstória 
criar_historico(1,1)
# reserva exemplo
criar_relatorio("mensal","2025-08-01","2025-08-31", gerado_por_bibliotecario=1)

print("Dados de exemplo inseridos (verifique ids e tabela).")

if __name__ == "__main__":
    popular()

