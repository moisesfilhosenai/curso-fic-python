import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()
alunos = cursor.execute(
    """
    SELECT * FROM alunos;
    """
)

for aluno in alunos.fetchall():
    nota1 = aluno[4]
    nota2 = aluno[5]
    print(f"Aluno {aluno[1]}, nota1 {nota1}, nota2 {nota2}")
    media = (nota1 + nota2) / 2
    aprovado = False

    if media > 5:
        aprovado = True

    cursor.execute(
        """
        UPDATE alunos
        SET media = ?, aprovado = ?
        WHERE id = ?
        """, (media, aprovado, aluno[0])
    )
    conexao.commit()

conexao.close()
