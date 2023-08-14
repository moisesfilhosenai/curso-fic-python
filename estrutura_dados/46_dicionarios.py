"""
Exemplo de dicionarios com python
"""

aluno = dict(nome="Sérgio", idade=18, cidade="Piracicaba")

print(f"O aluno tem as seguintes propriedades {aluno}")

aluno_eletrica = {
    "nome": "Elias",
    "idade": 26,
    "cidade": "Piracicaba",
    "curso": "elétrica",
    "disciplinas": ["CLP", "Comando elétricos", "Hidráulica"],
    "matriculado": True
}

print(f"O aluno tem as seguintes propriedades {aluno_eletrica}")

# Acessando propriedades
print(f"O aluno da elétrica chama-se {aluno_eletrica.get('nome')}")

print(f"O aluno tem {aluno['idade']} anos")

print(f"O aluno está no curso de {aluno.get('curso', 'Não existe a propriedade')}")

# Removendo elementos
del aluno_eletrica['idade']

print(f"O aluno tem as seguintes propriedades {aluno_eletrica}")