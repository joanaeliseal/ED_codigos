from ab import Arvore

if __name__ == "__main__":
    a = Arvore()
    a.add(100)
    a.add(200)
    a.add(300)
    a.add(50)
    a.add(150)
    assert a.raiz.valor == 100
    assert a.raiz.filho_direita.valor == 200
    assert a.raiz.filho_direita.filho_direita.valor == 300
    assert a.raiz.filho_esquerda.valor == 50
    assert a.raiz.filho_direita.filho_esquerda.valor == 150
    a.print()
    assert a.busca(289) == False
    a.remocao(150)
    assert a.raiz.filho_direita.filho_esquerda is None
