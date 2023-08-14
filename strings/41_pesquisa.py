"""
Exemplo de pesquisa de palavras no texto
"""

frase = "O curso de python é muito interessante"

print("Dentro da frase %s tem a palavra python %s " % (frase, "python" in frase))

print("Dentro da frase %s tem a palavra legal %s " % (frase, "legal" in frase))


endereco = "Rua 13 de maio, 459"

print("Dentro do endereço %s o número 459 inicia no index %d " % (endereco, endereco.find("459")))

print("Dentro do endereço %s o número 459 inicia no index da esquerda para direita %d "
      % (endereco, endereco.rfind("459")))