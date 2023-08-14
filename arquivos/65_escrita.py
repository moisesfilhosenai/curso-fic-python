"""
Exemplo de criação de arquivo vom Python

MODO      OPERAÇÂO
r         leitura
w         escrita
a         escrita, mas preserva o conteúdo
"""

nome_arquivo = "docs/numeros.txt"
arquivo = open(nome_arquivo, "w")

for linha in range(1, 101):
    arquivo.write("%d\n" % linha)

arquivo.close()
