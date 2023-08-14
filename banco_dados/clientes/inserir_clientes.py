import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
cursor.execute(
    """
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Alfredo Santos', 35, '123123123', 'alfredo@gmail.com', '19-91212-1212', 'Sao Paulo', 'SP', '2023-07-11')
    """
)
cursor.execute(
    """
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Maria Santos', 35, '123123123', 'maria@yahoo.com', '19-91212-1212', 'Sao Paulo', 'RJ', '2023-07-11')
    """
)
cursor.execute(
    """
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Elias Santos', 35, '123123123', 'elias@yahoo.com', '19-91212-1212', 'Sao Paulo', 'SP', '2023-07-11')
    """
)
conexao.commit()

conexao.close()
