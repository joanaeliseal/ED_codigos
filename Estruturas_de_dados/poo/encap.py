class Aluno:

    def __init__(self, nome, idade, telefone="9999-999"):
        self.nome = nome
        self.__idade = idade
        self._telefone = telefone

    def __repr__(self):
        return f'Aluno({self.nome})'
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, valor):
        if valor > 0:
            self.__idade = valor


a = Aluno("Rodrigo", 38)

class Relogio:

    def __init__(self):
        self.segundos = 90

    @property
    def minutos(self):
        self._xpto = 11
        return self.segundos // 60
    
    @minutos.setter
    def minutos(self, valor):
        self.segundos = valor * 60