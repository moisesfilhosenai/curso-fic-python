class Aluno:

    def __init__(self, nome: str, idade: int, email: str, matricula: int):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.matricula = matricula

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, value):
        self.nome = value
