"""
Exemplo de uso de for com python utilizando um dicionário
for <nome da variável> in <iterável>
"""

aluno = {
    "nome": "Elias",
    "idade": 26,
    "cidade": "Piracicaba",
    "curso": "elétrica",
    "matriculado": True
}

for chave, valor in aluno.items():
    print(f"Chave: {chave}, Valor: {valor}")

