import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()
cursor.execute(
    """
    CREATE TABLE alunos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ra INTEGER NOT NULL,
        email TEXT NOT NULL,
        nota1 INTEGER NOT NULL,
        nota2 INTEGER NOT NULL,
        media INTEGER DEFAULT 0,
        aprovado BOOLEAN DEFAULT FALSE
    );
    """
)
print("Tabela criada com sucesso")

conexao.close()
