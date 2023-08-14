"""
Exemplo de uso de while comparando numeros em python
Imprimir os números pares de 1 até 100
"""

incremento = 1

while incremento <= 100:
    if (incremento % 2) == 0:
        print(f"O número {incremento} é par")

    incremento += 1
