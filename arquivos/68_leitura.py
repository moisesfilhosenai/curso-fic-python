"""
Leitura de arquivo em Python com operador de contexto with
"""

nome_arquivo = "docs/alunos.txt"

with open(nome_arquivo, "r", encoding="UTF8") as file:
    for aluno in file.readlines():
        print(f"Aluno {aluno}")
