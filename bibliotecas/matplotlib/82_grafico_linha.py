"""
Exemplo de leitura de arquivo csv com Python
"""

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

filename = '../../dados_externos/2022/INMET_CO_DF_A001_BRASILIA_01-01-2022_A_31-12-2022.CSV'
dados = pd.read_csv(filename, skiprows=8, encoding="latin-1", on_bad_lines='skip', delimiter=';')

# print(f'DATAFRAME: {dataframe.head()}')
# print(f"Horarios {dataframe.columns}")
# print(f"Datas {dataframe['Data']}")
# print(f"Datas {dataframe['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']}")

meses = [
    {'mes_numero': 1, 'mes_nome': 'Jan', 'total_chuva': 0.0},
    {'mes_numero': 2, 'mes_nome': 'Fev', 'total_chuva': 0.0},
    {'mes_numero': 3, 'mes_nome': 'Mar', 'total_chuva': 0.0},
    {'mes_numero': 4, 'mes_nome': 'Abr', 'total_chuva': 0.0},
    {'mes_numero': 5, 'mes_nome': 'Mai', 'total_chuva': 0.0},
    {'mes_numero': 6, 'mes_nome': 'Jun', 'total_chuva': 0.0},
    {'mes_numero': 7, 'mes_nome': 'Jul', 'total_chuva': 0.0},
    {'mes_numero': 8, 'mes_nome': 'Ago', 'total_chuva': 0.0},
    {'mes_numero': 9, 'mes_nome': 'Set', 'total_chuva': 0.0},
    {'mes_numero': 10, 'mes_nome': 'Out', 'total_chuva': 0.0},
    {'mes_numero': 11, 'mes_nome': 'Nov', 'total_chuva': 0.0},
    {'mes_numero': 12, 'mes_nome': 'Dez', 'total_chuva': 0.0},

]

for index, row in dados.iterrows():
    data = datetime.strptime(row['Data'], '%Y/%m/%d').date()
    mes_numero = data.month

    chuva = str(row['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'])
    chuva = chuva.replace(",", ".")
    chuva = float(chuva)

    for mes in meses:
        if mes['mes_numero'] == mes_numero:
            mes['total_chuva'] += chuva

# print(f"Chuvas {meses}")

dados_grafico = [
    [], []
]

for mes in meses:
    dados_grafico[0].append(mes['mes_numero'])
    dados_grafico[1].append(mes['total_chuva'])

# print(f"PLOT {dados_grafico}")

# define o tamanho figsize=(largura, altura)
plt.figure(figsize=(10, 5))

# passa as informações eixo x e y
plt.plot(dados_grafico[0], dados_grafico[1])

plt.title('Informações Chuvas de 2022')
plt.xlabel('Meses')
plt.ylabel('Valores')

# exibe todos os valores no eixo
plt.xticks(dados_grafico[0])

plt.savefig("chuvas_anuais.png")
plt.close("all")