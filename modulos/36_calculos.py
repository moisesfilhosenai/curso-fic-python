"""
Exemplo de uso de módulo calculadora com from
"""

from calculadora import somar, subtrair, multiplicar, dividir

soma = somar(10, 20)
print(f"O resultado da soma é {soma}")

subtracao = subtrair(10, 20)
print(f"O resultado da subtração é {subtracao}")

multiplicacao = multiplicar(10, 20)
print(f"O resultado da multiplicação é {multiplicacao}")

divisao = dividir(10, 20)
print(f"O resultado da divisão é {divisao}")
