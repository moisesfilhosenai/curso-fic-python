"""
Exemplo de utilização da estrutura de dado Série com pandas
"""
import pandas as pd

notas = [3.9, 2.0, 1.3, 7.8, 9.0]

serie = pd.Series(data=notas)
print(f"A informação contida na série é \n{serie}")

serie_index = pd.Series(data=notas, index=[10, 11, 12, 13, 14])
print(f"A informação contida na série é \n{serie_index}")

notas_alunos = {
    "aluno1": 4.8,
    "aluno2": 5.3,
    "aluno3": 8.9,
    "aluno4": 9.9
}

serie_alunos = pd.Series(notas_alunos)
print(f"A informação contida na série de alunos é \n{serie_alunos}")

serie_nomeada = pd.Series(data=["gol", "palio", "uno"], name="Carros")
print(f"A informação da série é \n{serie_nomeada}")
