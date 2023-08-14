"""
Exemplo de manipulação dos dados com pandas
Monta um dicionário de temperaturas no formato:
{1: [], 2: [],3: []}
"""

from random import randint
import pandas as pd

temperaturas = {}

for dia in range(1, 31):
    chave = "dia_" + str(dia)
    temperaturas[chave] = []
    for periodo in range(1, 25):
        temperatura = randint(5, 38)
        temperaturas[chave].append(temperatura)

dataframe = pd.DataFrame(temperaturas)

# Head mostra as informações iniciais do dataframe
print(f"Informações com head \n{dataframe.head()}")

# Tail mostra as informações definindo o número de linhas a serem exibidas
print(f"Informações com tail \n{dataframe.tail(3)}")

# Describe faz uma estatística das informações do dataframe
# mean (média), std (desvio padrão)
print(f"Informações com describe \n{dataframe.describe()}")

