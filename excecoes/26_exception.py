"""
Exemplo de tratamento de erros com exception
"""


def soma(n1, n2):
    resultado = n1 + n2
    return resultado


try:
    numero1 = 10
    numero2 = "b"
    soma(numero1, numero2)
except Exception as ex:
    print("Erro ao realizar cálculo", ex)
