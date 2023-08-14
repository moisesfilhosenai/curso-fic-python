import matplotlib.pyplot as plt
import pandas as pd


dataframe = pd.read_csv('../dados_externos/chuvas_jan_2023.csv', delimiter=';')

# define o tamanho figsize=(largura, altura)
plt.figure(figsize=(10, 5))

# passa as informações eixo x e y
plt.plot(dataframe['DIA'], dataframe['VALOR'])

plt.title('Informações Chuvas Janeiro de 2023')
plt.xlabel('Dias')
plt.ylabel('Valores')

# exibe todos os valores no eixo
plt.xticks(dataframe['DIA'])

plt.savefig("chuvas_jan_2023.png")
plt.close("all")
