import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()
cursor.execute(
    """
    INSERT INTO alunos (nome, ra, email, nota1, nota2)
    VALUES ('Alfredo Santos', 1234, 'alfredo@gmail.com', 4, 6)
    """
)
cursor.execute(
    """
    INSERT INTO alunos (nome, ra, email, nota1, nota2)
    VALUES ('Eliza Santos', 6734, 'eliza@gmail.com', 2, 10)
    """
)
cursor.execute(
    """
    INSERT INTO alunos (nome, ra, email, nota1, nota2)
    VALUES ('Danilo Santos', 12875, 'danilo@gmail.com', 5, 7)
    """
)
conexao.commit()

conexao.close()
