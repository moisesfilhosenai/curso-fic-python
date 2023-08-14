from zipfile import ZipFile
import os
import shutil

# cria uma pasta par armazenar os arquivos
os.mkdir("../dados_externos/arquivos_saida")

alunos = ["João", "Maria", "Silvia"]
nome_arquivo = "../dados_externos/arquivos_saida/alunos.txt"

with open(nome_arquivo, "w", encoding="UTF8") as file:
    for aluno in alunos:
        file.write(f"{aluno} \n")

filename = "../dados_externos/output"

# shutil.make_archive(‘output file name’, ‘zip’, ‘directory name’)
shutil.make_archive(filename, "zip", "../dados_externos/arquivos_saida")

