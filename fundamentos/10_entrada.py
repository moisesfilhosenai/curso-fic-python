"""
Exemplo de código que utiliza as entradas float com input
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("A média para as notas %2.2f e %2.2f foi: %2.2f" % (nota1, nota2, media))
