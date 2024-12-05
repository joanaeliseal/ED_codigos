class NodeNotFound(Exception):
    pass

class Node:

    def __init__(self, valor):
        self.valor = valor
        self.filho_esquerda: Node|None = None
        self.filho_direita: Node|None = None

    def __repr__(self):
        return f'No(valor={self.valor})'

    def add_esquerda(self, valor):
        if self.filho_esquerda is None:
            self.filho_esquerda = Node(valor)

    def add_direita(self, valor):
        if self.filho_direita is None:
            self.filho_direita = Node(valor)

    @property
    def tem_filho_esquerda(self) -> bool:
        return bool(self.filho_esquerda)

    @property
    def tem_filho_direita(self) -> bool:
        return bool(self.filho_direita)

    @property
    def eh_folha(self) -> bool:
        return not self.tem_filho_direita and not self.tem_filho_esquerda


class Arvore:

    def __init__(self):
        self.raiz: Node|None = None

    @property
    def vazia(self) -> bool:
        return self.raiz is None

    def add(self, valor):
        self.raiz = self._add(self.raiz, valor)

    def _add(self, no: Node|None, valor):
        if no is None:
            return Node(valor)
        if valor > no.valor:
            no.filho_direita = self._add(no.filho_direita, valor)
        else:
            no.filho_esquerda = self._add(no.filho_esquerda, valor)
        return no

    def print(self):
        if not self.vazia:
            self._print_pre_ordem(self.raiz)

    def _print_pre_ordem(self, no: Node|None):
        if no is None:
            return
        print(no.valor)
        self._print_pre_ordem(no.filho_esquerda)
        self._print_pre_ordem(no.filho_direita)

    def _print_em_ordem(self, no: Node|None):
        if no is None:
            return
        self._print_em_ordem(no.filho_esquerda)
        print(no.valor)
        self._print_em_ordem(no.filho_direita)

    def _print_pos_ordem(self, no: Node|None):
        if no is None:
            return
        self._print_pos_ordem(no.filho_esquerda)
        self._print_pos_ordem(no.filho_direita)
        print(no.valor)

    def busca(self, valor) -> bool:
        return self._busca(self.raiz, valor)

    def _busca(self, no: Node|None, valor) -> bool:
        if no is None:
            return False
        elif no.valor == valor:
            return True
        elif valor > no.valor:
            return self._busca(no.filho_direita, valor)
        else:
            return self._busca(no.filho_esquerda, valor)

    def count(self):
        return self._count(self.raiz)

    def _count(self, no:Node|None):
        if no is None:
            return 0

        return 1 +\
            self._count(no.filho_esquerda) +\
            self._count(no.filho_direita)

    @property
    def altura(self) -> int:
        return self._altura(self.raiz)

    def _altura(self, no:Node|None) -> int:
        if no is None:
            return 0

        alt_esquerda = self._altura(no.filho_esquerda)
        alt_direita = self._altura(no.filho_direita)
        return 1 + max(alt_esquerda, alt_direita)

    @property
    def leafs(self) -> int:
        return self._leafs(self.raiz)

    def _leafs(self, no: Node|None) -> int:
        if no is None:
            return 0

        if no.eh_folha:
            return 1

        return self._leafs(no.filho_esquerda) + self._leafs(no.filho_direita)

    def get_level(self, key) -> int:
        return self._get_level(self.raiz, key, nivel=0)

    def _get_level(self, no: Node|None, key, nivel) -> int:
        if no is None:
            raise NodeNotFound()
        elif no.valor == key:
            return nivel
        elif key > no.valor:
            return self._get_level(no.filho_direita, key, nivel+1)
        else:
            return self._get_level(no.filho_esquerda, key, nivel+1)


    def liberar(self, valor) -> bool:
        return self._liberar(self.raiz, valor)

    def _liberar(self, no: Node | None, valor) -> bool:
        if no is None:
            return False
        elif no.valor == valor:
            no.filho_esquerda = None
            no.filho_direita = None
            return True
        elif valor > no.valor:
            return self._liberar(no.filho_direita, valor)
        else:
            return self._liberar(no.filho_esquerda, valor)

    def _get_sucessor(self, no: Node) -> Node:
        atual: Node = no
        while atual.tem_filho_esquerda:
            atual = atual.filho_esquerda
        return atual

    def remocao(self, valor):
        self.raiz = self._remocao(self.raiz, valor)

    def _remocao(self, no: Node|None, valor) -> Node|None:
        if no is None:
            return None

        if valor < no.valor:
            no.filho_esquerda = self._remocao(no.filho_esquerda, valor)
        elif valor > no.valor:
            no.filho_direita = self._remocao(no.filho_direita, valor)
        else:
            if not no.tem_filho_direita:
                return no.filho_esquerda
            elif not no.tem_filho_esquerda:
                return no.filho_direita
            else:
                substituto = self._get_sucessor(no.filho_direita)
                no.valor = substituto.valor
                no.filho_direita = self._remocao(no.filho_direita, no.valor)

        return no
