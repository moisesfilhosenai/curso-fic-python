"""
Exemplo de função com parâmetros nomeados
"""


def calcula_aumento_salario(salario, percentual_aumento):
    salario_com_aumento = salario + (salario * percentual_aumento / 100)
    return salario_com_aumento


salario_atual = 2500
percentual = 10

salario_novo = calcula_aumento_salario(percentual_aumento=percentual, salario=salario_atual)
valor_aumento = salario_novo - salario_atual

print("As informações do salário ficaram assim: salário antigo R$ %5.2f, salário atual R$ %5.2f, "
      "percentual aumento %d, valor do aumento R$ %5.2f " % (salario_atual, salario_novo, percentual, valor_aumento))
