"""
Exemplo de uso de while comparando numeros em python
Imprimir os números pares de 1 até 100
Deve contar a quantidade de números e se chegar até 10 unidades parar o laço
"""

incremento = 1
contador_unidades = 0

while incremento <= 100:
    if (incremento % 2) == 0:
        print(f"O número {incremento} é par")
        contador_unidades += 1

    if contador_unidades == 10:
        break

    incremento += 1
