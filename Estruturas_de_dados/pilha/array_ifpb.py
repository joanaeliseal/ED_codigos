

class Array:
    
    def __init__(self, tamanho: int):
        self.tamanho = tamanho
        self._dados = [None] * tamanho

    def _check_posicao(self, posicao):
        if not posicao >= 0:
            raise IndexError("posicao inválida")
        
    def set(self, posicao: int, valor):
        self._check_posicao(posicao)
        self._dados[posicao] = valor

    def __setitem__(self, posicao: int, valor):
        self.set(posicao, valor)
    
    def get(self, posicao: int):
        self._check_posicao(posicao)
        return self._dados[posicao]
    
    def __getitem__(self, posicao: int):
        return self.get(posicao)
    
    def copiar_de(self, outro_array):
        for i in range(outro_array.tamanho):
            self.set(i, outro_array.get(i))
    

# a = Array(10)    
# a[1] = "abc"
# print(a[1])