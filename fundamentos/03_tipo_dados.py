
"""
Exemplo de declaração de variaveis com diferentes valores
"""

nome = "Alfredo"
sobrenome = "Alves"
idade = 40
esta_empregado = True
salario = 5.29
dados = [1, 4, "A", False]
dicionario = {"estudar": True, "tempo": "calor"}
nada = None

"""
strings são uma cadeia de caracteres que pode ser manipulada facilmente
- Contagem de palavras
- Encontrar letra pelo índice
- Concatenar palavras formando textos
"""

cidade = "Piracicaba"
print("A cidade ", cidade, " tem ", len(cidade), " letras")

indice_nove = cidade[9]
print("O indice nove da palavra ", cidade, " é a letra ", indice_nove)

estado = "São Paulo"
cidade_estado = "A cidade de " + cidade + " fica no estado de " + estado
print(cidade_estado)

"""
Fazendo composição de strings de forma inteligente, argumentos:
%d para números inteiros
%s para strings
%f números decimais
%f5.2 onde os números antes e depois do ponto formatam as casas decimais
"""

print("Senhor %s tem %d anos, trabalha e ganha R$%5.2f de salário" % (nome, idade, salario))

"""
Fazendo a formatação da saida de outras formas
"""

print(f"Senhor {nome} tem {idade} anos, trabalha e ganha R$ {salario}")

print("Senhor {0} tem {1} anos, trabalha e ganha R$ {2}".format(nome, idade, salario))
