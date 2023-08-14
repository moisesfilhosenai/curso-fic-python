class Atividade:
    def __init__(self, descricao: str, nota_maxima=10.0):
        self.descricao = descricao
        self.nota_maxima = nota_maxima

    def __str__(self):
        return f"A atividade {self.descricao} tem a nota máxima de {self.nota_maxima}"
