from array_ifpb import Array


class ListaCheiaException(Exception):
	pass


class ListaVaziaException(Exception):
	pass


class Lista:

	@property
	def vazia(self):
		...

	def __len__(self):
		...

	def __str__(self):
		...

	def __repr__(self):
		return str(self)

	def imprimir(self):
		return print(self)

	def inserir(self, posicao, valor):
		...

	def remover(self, posicao):
		...

	def obter(self, posicao):
		...

	def atribuir(self, posicao, valor):
		self._dados[posicao] = valor

	def __getitem__(self, posicao):
		return self.obter(posicao)

	def __setitem__(self, posicao, valor):
		self.atribuir(posicao, valor)


class ListaSimples(Lista):

	def __init__(self):
		self._dados = []

	@property
	def vazia(self):
		return len(self) == 0

	def __len__(self):
		return len(self._dados)

	def __str__(self):
		return str(self._dados)

	def inserir(self, posicao, valor):
		self._dados.insert(posicao, valor)

	def remover(self, posicao):
		self._dados.pop(posicao)

	def obter(self, posicao):
		return self._dados[posicao]


class ListaSequencial(Lista):

	def __init__(self, tamanho=10):
		self._quantidade: int = 0
		self._dados = Array(tamanho)

	@property
	def cheia(self):
		return self._quantidade == self._dados.tamanho

	@property
	def vazia(self):
		return len(self) == 0

	def __len__(self):
		return self._quantidade

	def __str__(self):
		s = "["
		for i in range(self._quantidade):
			s += repr(self._dados[i])
			if i < self._quantidade - 1:
				s += ", "

		s += "]"
		return s

	def _deslocar_direita(self, posicao):
		for i in range(self._quantidade, posicao, -1):
			self._dados[i] = self._dados[i - 1]

	def _deslocar_esquerda(self, posicao):
		for i in range(posicao, self._quantidade - 1):
			self._dados[i] = self._dados[i+1]

	def _get_posicao(self, posicao):
		if posicao < 0:
			return len(self) - posicao
		return posicao

	def inserir(self, posicao, valor):
		posicao = self._get_posicao(posicao)
		if self.cheia:
			raise ListaCheiaException()

		if posicao >= len(self):
			self._dados[self._quantidade] = valor
		else:
			self._deslocar_direita(posicao)
			self._dados[posicao] = valor

		self._quantidade += 1

	def obter(self, posicao):
		posicao = self._get_posicao(posicao)
		return self._dados[posicao]

	def remover(self, posicao):
		if self.vazia:
			raise ListaVaziaException()

		posicao = self._get_posicao(posicao)
		if posicao < len(self):
			self._deslocar_esquerda(posicao)
		self._quantidade -= 1


class Node:

	def __init__(self, valor, proximo=None):
		self.valor = valor
		self.proximo = proximo


class ListaEncadeada(Lista):

	def __init__(self):
		self.head: Node|None = None
		self._quantidade = 0

	@property
	def vazia(self):
		return self._quantidade == 0

	@property
	def cheia(self):
		return False

	def __len__(self):
		return self._quantidade

	def _get_no_indice(self, posicao):
		if posicao >= len(self):
			raise IndexError()
		no = self.head
		for i in range(posicao):
			no = no.proximo
		return no

	def get_antecessor(self, posicao):
		return self._get_no_indice(posicao - 1)

	def inserir(self, posicao, valor):
		posicao = self._get_posicao(posicao)
		novo = Node(valor)
		if self.vazia:
			self.head = novo
		elif posicao == 0:
			novo.proximo = self.head
			self.head = novo
		else:
			antecessor = self.get_antecessor(posicao)
			novo.proximo = antecessor.proximo
			antecessor.proximo = novo

		self._quantidade += 1

	def remover(self, posicao):
		posicao = self._get_posicao(posicao)
		if self.vazia:
			raise ListaVaziaException()

		if posicao == 0:
			self.head = self.head.proximo
		else:
			antecessor = self.get_antecessor(posicao)
			antecessor.proximo = antecessor.proximo.proximo

		self._quantidade -= 1

	def __str__(self):
		s = "["
		no = self.head
		for i in range(self._quantidade):
			s += repr(no.valor)
			if i < self._quantidade - 1:
				s += ", "
			no = no.proximo
		s += "]"
		return s


	def _get_posicao(self, posicao):
		if posicao < 0:
			return len(self) - posicao
		return posicao

	def obter(self, posicao):
		posicao = self._get_posicao(posicao)
		no = self._get_no_indice(posicao)
		return no.valor

	def atribuir(self, posicao, valor):
		posicao = self._get_posicao(posicao)
		no = self._get_no_indice(posicao)
		no.valor = valor





