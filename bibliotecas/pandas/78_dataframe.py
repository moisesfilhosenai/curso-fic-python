"""
Exemplo da estrutura de dados Dataframe com pandas
"""

import pandas as pd

notas_alunos = {
    "alunos": pd.Series(data=["aluno1", "aluno2", "aluno3"]),
    "notas_p1": pd.Series(data=[2.9, 1.2, 9.0]),
    "notas_p2": pd.Series(data=[4.8, 2.2, 7.1])
}

dataframe = pd.DataFrame(notas_alunos)
print(f"Exibindo todos os alunos \n{dataframe}")

dataframe_filtro1 = pd.DataFrame(notas_alunos, index=[1, 2])
print(f"Exibindo alunos no índice 1 e 2 \n{dataframe_filtro1}")

dataframe_filtro2 = pd.DataFrame(notas_alunos, columns=["alunos", "notas_p2"])
print(f"Exibindo somente as colunas alunos e notas p2 \n{dataframe_filtro2}")

