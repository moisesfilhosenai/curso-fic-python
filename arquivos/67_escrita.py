"""
Escrita de arquivo em python com operador de contexto with
"""

alunos = ["João", "Maria", "Silvia"]
nome_arquivo = "docs/alunos.txt"

with open(nome_arquivo, "w", encoding="UTF8") as file:
    for aluno in alunos:
        file.write(f"{aluno} \n")

