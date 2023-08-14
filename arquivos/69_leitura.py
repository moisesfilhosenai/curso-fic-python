"""
Leitura de arquivo em Python com operador de contexto with
"""

nome_arquivo = "docs/aluno.txt"

try:
    with open(nome_arquivo, "r", encoding="UTF8") as file:
        for aluno in file.readlines():
            print(f"Aluno {aluno}")
except FileNotFoundError:
    print(f"O arquivo {nome_arquivo} não foi encontrado :(")