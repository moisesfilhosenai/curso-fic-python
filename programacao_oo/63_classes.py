"""
Exemplo de uso de classes com python
"""

from carro import Carro
from aluno import Aluno
from disciplina import Disciplina
from atividade import Atividade
from cidade import Cidade

carro1 = Carro()
print(f"O carro {carro1.modelo} é da marca {carro1.marca} com a cor {carro1.cor}, "
      f"ano de fabricação {carro1.ano_fabricacao}, possui rodas ? {carro1.tem_rodas}")

aluno1 = Aluno("Matias Santos", 19, "matias@gmail.com", 123456)
print(f"O aluno {aluno1.nome} tem {aluno1.idade}, seu e-mail é {aluno1.email} "
      f"e a matrícula {aluno1.matricula}")

poo = Disciplina(termo=1, nome="Programação Orientada a Objetos")
print(f"A disciplina de {poo.nome} está aprovada ? {poo.aprovada}")
poo.aprovar()
print(f"A disciplina de {poo.nome} está aprovada ? {poo.aprovada}")
poo.atribuir_curso("Lógica de programação")
print(f"A disciplina de {poo.nome} é do curso {poo.curso}")

atividade_poo = Atividade("Criar classes em POO")
print(atividade_poo)
atividade_logica = Atividade(descricao="Criar algoritmo para média", nota_maxima=8)
print(atividade_logica)

piracicaba = Cidade(nome="piracicaba", uf="sp")
piracicaba.nome = "PIRACICABA"
piracicaba.uf = "SP"
print(f"A cidade de {piracicaba.nome} é do estado de {piracicaba.uf}")

