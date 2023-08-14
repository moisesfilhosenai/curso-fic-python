import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
clientes = cursor.execute(
    """
    SELECT * FROM clientes;
    """
)

for cliente in clientes.fetchall():
    print(f"Cliente {cliente[1]}, email {cliente[4]}")

conexao.close()
