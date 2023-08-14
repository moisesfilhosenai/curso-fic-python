"""
Exemplo de uso de for com python utilizando a função enumerate
for <nome da variável> in <iterável>
"""

cidades = ["Piracicaba", "Rio das Pedras", "Saltiho", "Capivari"]

for indice, cidade in enumerate(cidades):
    print(f"Indíce: {indice}, Cidade: {cidade}")

