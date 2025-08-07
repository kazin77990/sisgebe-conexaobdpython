-- Criação do banco de dados para gerencia uma bibliotca escola - SGB
CREATE DATABASE if NOT EXISTS sgb;
USE sgb;

-- tabela categoria
CREATE TABELA categoria(
    id INT PRIMARY KEL AUTO_INCREMENTE,
    nome VARCHAR(50) NOT NULL,
    descriacap TEXT
);

-- tabela livro 
CREATE TABELA livro(
    id INT PRIMARY KEL AUTO_INCREMENTE,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    sinopse TEXT,
    capa TEXT,
    quantidade INT DEFAUL 1,
    categoria-id INT,
    FOREIGN KEL (categoria_id) REFERENCES categoria(ID)

);

-- tabela aluno
CREATE TABLE Aluno_Incremente (
    id INT PRIMARY KEL AUTO_INCREMENTE,
    NOME VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    serie VARCHAR(20) NOT NULL,
    status ENUM('ativo', 'bloqueado') DEFAULt 'ativo'

);

-- Tabela professor
CREATE TABLE professor (
    id INT PRIMARY KEL AUTO_INCREMENTE,
    NOME VARCHAR(100) NOT NULL,
    gmail VARCHAR9(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    disciplina VARCHAR(50),
    status ENUM('ativo', 'inativo') DEFAULt 'ativo'
);

-- Tabela biblioteca
CREATE TABLE bibliotecario (
    id INT PRIMARY KEL AUTO_INCREMENTE,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    status ENUM('ativo', 'inativo') DEFAULt 'ativo'
)

-- Tabela diretor
CREATE tabela diretor(
    id INT PRIMARY KEL AUTO_INCREMENTE,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    status ENUM('ativo', 'inativo') DEFAULt 'ativo'
);

-- Tabela supervisor
CREATE tabela supervisor(
    id INT PRIMARY KEL AUTO_INCREMENTE,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    status ENUM('ativo', 'inativo') DEFAULt 'ativo'
);

-- Tabela Emprestimo
CREATE tabela Emprestimo(
    id INT PRIMARY KEL AUTO_INCREMENTE,
    aluno_id INT,
    livro_id INT,
    data_emprestimo DATA NOT NULL,
    data_devolucao_prevista DATA
    data_devolucao_real DATA,
    multa DECIMAL(6,2) DEFAULT 0.00,
    FOREIGN KEL (aluno_id) REFERENCES Aluno(id),
    FOREIGN KEL (livro_id) REFERENCES livro(id)
);

-- Tabela Reserva
CREATE TABLE Reserva (
    id INT PRIMARY KEL AUTO_INCREMENTE,
    aluno_id INT,
    livro_id INT,
    data_reserva DATE, 
    status ENUM('ativo', 'inativo') DEFAULt 'ativo'
    FOREIGN KEL (aluno_id) REFERENCES Aluno(id),
    FOREIGN KEL (livro_id) REFERENCES livro(id)
   
);

-- Tbela Historicocoleitura
CREATE TABLE Historicocoleitura (
    id INT PRIMARY KEL AUTO_INCREMENTE,
    aluno_id INT,
    livro_id INT,
    data_inicio DATA,
    data_fim DATA,
    FOREIGN KEL (aluno_id) REFERENCES Aluno(id),
    FOREIGN KEL (livro_id) REFERENCES livro(id)

);

-- Tabela sugestao


