"""
Exemplo de código que utiliza as entradas int com input
"""

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")

media = (int(nota1) + int(nota2)) / 2

print("A média para as notas %s e %s foi: %2.2f" % (nota1, nota2, media))
