"""
Exemplo de uso de for com python
for <nome da variável> in <iterável>

Precisa utilizar a função range para iterar
O range vai até o número-1, no caso do exemplo até 50 usando passo de 5 em 5
A função builtin range do python gera uma sequencia de números
"""

# range(inicio, fim, passo)
for incremento in range(10, 51, 5):
    print(f"Estou utilizando o laço for para incrementar o valor: {incremento}")

