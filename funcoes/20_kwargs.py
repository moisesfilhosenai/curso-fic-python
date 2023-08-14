"""
Exemplo de função com multiplos parametros kwargs
"""


def calcula_salario(salario_base, **kwargs):
    """
    Função que calcula o salário liquido baseado nos descontos
    :param salario_base:
    :param kwargs:
    :return:
    """
    desconto_inss = kwargs.get("inss") / 100
    desconto_plano_saude = kwargs.get("plano")
    total_descontos = desconto_inss + desconto_plano_saude
    salario_liquido = salario_base - total_descontos
    return salario_liquido


salario_atual = 3780
INSS = 8
plano = 129.90
salario_receber = calcula_salario(salario_atual, inss=INSS, plano=plano)

print(" O resumo do salário ficou assim:\n Desconto INSS: %d \n Desconto Plano de saúde: R$% 5.2f "
      "\n Salário a receber: R$% 5.2f" % (INSS, plano, salario_receber))

