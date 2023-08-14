"""
Exemplo de tratamento de erros com exception utilizando IndexError
"""


try:
    numeros = [1, 60, 40, 30, 10]
    print("O numero na posição 5 é: %d" % numeros[5])
except IndexError as ex:
    print("Erro ao acessar indíce", ex)
