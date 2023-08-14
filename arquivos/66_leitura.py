"""
Exemplo de leitura de arquivo com Python
"""

arquivo = open("docs/numeros.txt", "r")

for linha in arquivo.readlines():
    print(linha)

arquivo.close()
