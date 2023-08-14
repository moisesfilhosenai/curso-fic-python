class Cidade:

    def __init__(self, nome: str, uf: str):
        self.__nome = nome
        self.__uf = uf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, value):
        self.__uf = value
