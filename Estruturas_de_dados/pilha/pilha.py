from array_ifpb import Array

class Pilha:
    def __init__(self):
        ...

    def empilhar(self, elemento):
        ...

    def desempilhar(self):
        ...

    def imprimir(self):
        ...

    @property
    def topo(self):
        ...


class PilhaFacil:
    def __init__(self):
        self._dados = []

    def empilhar(self, elemento):
        self._dados.append(elemento)

    def desempilhar(self):
        return self._dados.pop()
    
    def imprimir(self):
        for elemento in self._dados:
            print(elemento, end=" ")
        print()

    @property
    def topo(self):
        return self._dados[-1]

    
class PilhaVazia(Exception):
    pass

class PilhaCheia(Exception):
    pass

class PilhaSequencial:

    def __init__(self):
        self._dados = Array(tamanho=3)
        self._topo = 0

    @property
    def tamanho(self):
        return self._topo

    @property
    def vazia(self):
        return self.tamanho == 0
    
    @property
    def cheia(self):
        return self.tamanho == self._dados.tamanho
    
    def _redimensionar(self):
        dados_velhos = self._dados
        dados_novos = Array(dados_velhos.tamanho * 2)
        self._dados = dados_novos
        self._dados.copiar_de(dados_velhos)

    def empilhar(self, elemento):
        if self.cheia:
            self._redimensionar()
        
        self._dados.set(self._topo, elemento)
        self._topo += 1

    def desempilhar(self):
        if self.vazia:
            raise PilhaVazia()

        topo = self.topo
        self._topo -= 1
        self._dados.set(self._topo, None)
        return topo

    def imprimir(self):
        for i in range(self._topo):
            print(self._dados.get(i), end=" ")
        print()

    @property
    def topo(self):
        if self.vazia:
            raise PilhaVazia()
        return self._dados.get(self._topo - 1)
    


class Node:

    def __init__(self, valor, proximo: 'Node' = None):
        self.valor = valor
        self.proximo = proximo
    

class PilhaEncadeada:
    
    def __init__(self):
        self._topo: None|Node = None
        self._tamanho = 0

    @property
    def tamanho(self):
        return self._tamanho
    
    @property
    def vazia(self):
        return self.tamanho == 0
    
    def empilhar(self, elemento):
        self._topo = Node(elemento, proximo=self._topo)
        self._tamanho += 1

    def desempilhar(self):
        if self.vazia:
            raise PilhaVazia()
        
        self._topo = self._topo.proximo
        self._tamanho -= 1

    def imprimir(self):
        atual: Node = self._topo
        while atual:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()

    @property
    def topo(self):
        if self.vazia:
            raise PilhaVazia()
        return self._topo.valor




def test_pilha_facil():
    p = PilhaFacil()
    p.empilhar("1")
    assert p.topo == "1"
    p.empilhar("2")
    p.empilhar("3")
    assert p.desempilhar() == "3"
    assert p.desempilhar() == "2"
    assert p.desempilhar() == "1"


if __name__ == "__main__":
    test_pilha_facil()





    