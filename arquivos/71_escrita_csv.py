"""
Exemplo de escrita de arquivo csv em Python
"""

import csv

nome_arquivo = "docs/temperaturas.csv"
cabecalho = ["DIA DA SEMANA", "TEMPERATURA"]
nomes_campos = ["dia", "temperatura"]
dados = [
    {"dia": "segunda-feira", "temperatura": 29.4},
    {"dia": "terça-feira", "temperatura": 23.2},
    {"dia": "quarta-feira", "temperatura": 19.1},
    {"dia": "quinta-feira", "temperatura": 13.9},
    {"dia": "sexta-feira", "temperatura": 10.9},
    {"dia": "sábado", "temperatura": 12.8},
    {"dia": "domingo", "temperatura": 15.3},
]

with open(nome_arquivo, "w", encoding="UTF8", newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(cabecalho)

    for info in dados:
        escritor.writerow([info.get('dia'), info.get('temperatura')])
