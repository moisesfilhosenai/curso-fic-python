"""
Exemplo de criação de csv com python e pandas
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

dataframe.to_csv("temperaturas.csv")
