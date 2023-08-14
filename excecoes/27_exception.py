"""
Exemplo de tratamento de erros com exception e finally
"""


def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


try:
    n1 = 5.5
    resultado = calcular_media(n1, n2)
except Exception as ex:
    print("Ocorreu um erro ao calcular a média ", ex)
finally:
    print("Algoritmo finalizou")
