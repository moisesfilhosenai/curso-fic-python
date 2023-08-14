"""
Exemplo de uso de for com python utilizando list comprehension
for <nome da variável> in <iterável>
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = [numero for numero in numeros if numero % 2 == 0]

for numero_par in numeros_pares:
    print(f"O número par: {numero_par}")

