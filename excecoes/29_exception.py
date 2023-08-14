"""
Exemplo de tratamento de erros com exception utilizando várias exceptions
"""

try:
    nota1 = int(input("Digite a primeira nota"))
    nota2 = int(input("Digite a segunda nota"))
    fator = int(input("Digite o fator para calcular a média"))
    media = (nota1 + nota2) / fator
    print("A média é: %2.2f " % media)
except ValueError as ex:
    print("Erro ao calcular a media foi digitado um valor inválido ", ex)
except ZeroDivisionError as ex:
    print("Erro ao calcular a media, divisão por 0 ", ex)
except Exception as ex:
    print("Erro ao calcular a media ", ex)
