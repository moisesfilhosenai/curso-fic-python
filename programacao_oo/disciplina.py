class Disciplina:
    def __init__(self, nome: str, termo: int):
        self.nome = nome
        self.termo = termo
        self.aprovada = False
        self.curso = ""

    def aprovar(self):
        self.aprovada = True

    def atribuir_curso(self, curso):
        self.curso = curso
