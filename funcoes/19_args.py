"""
Exemplo de função com multiplos parâmetros args
"""


def imprimir_cidade_bairros(cidade, *args):
    print("A cidade %s tem os seguintes bairros:" % cidade)

    for bairro in args:
        print(bairro)


imprimir_cidade_bairros("Piracicaba", "Centro", "Vila Rezende", "Campestre", "Nova América")
