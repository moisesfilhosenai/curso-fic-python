"""
Exemplo do uso de listas com python
"""

numeros = [20, 56, 19, 40, 31]

print(f"A lista tem {len(numeros)} itens")

print(f"O index 2 da lista é o número {numeros[2]}")

"""
Alteração de elementos
"""

numeros[4] = 123

print(f"A lista contem os numeros {numeros}")

numeros.append(560)

print(f"A lista contem os numeros {numeros}")

del numeros[1]

print(f"A lista contem os numeros {numeros}")

"""
Fatiamento de elementos da lista
"""

numeros_novos = numeros[:3]
print(f"A lista contem os novos numeros {numeros_novos}")

numeros_novos_dois = numeros[2:]
print(f"A lista contem os novos numeros {numeros_novos_dois}")