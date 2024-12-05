from lista import ListaSimples, ListaSequencial, ListaEncadeada

def test_lista_simples():
	l = ListaSimples()
	assert len(l) == 0
	assert str(l) == "[]"
	assert l.vazia == True
	l.inserir(0, "abc")
	assert l.obter(0) == "abc"
	assert l[0] == "abc"
	l.remover(0)
	assert l.vazia
	l.inserir(0, 123)
	l.atribuir(0, 456)
	l[0] = 678
	assert l[0] == 678

def test_lista_sequencial():
	l = ListaSequencial()
	assert str(l) == "[]"
	assert len(l) == 0
	assert l.vazia
	l.inserir(1000, "abc")
	assert str(l) == "['abc']"
	assert l[0] == "abc"
	l.inserir(100, "def")
	l.inserir(100, "fgh")
	l.inserir(1, "funciona")
	assert l[1] == "funciona"
	l.remover(2)
	assert l[2] == "fgh"
	l.remover(2)
	assert len(l) == 2
	assert l[1] == "funciona"
	l.remover(0)
	assert len(l) == 1
	assert l[0] == "funciona"

def test_lista_encadeada():
	l = ListaEncadeada()
	assert l.vazia
	assert l.cheia == False
	l.inserir(1000, "abc")
	assert l.vazia == False
	assert l[0] == "abc"
	l.inserir(1000, "def")
	assert l[1] == "def"
	l.inserir(1000, "fgh")
	assert l[2] == "fgh"
	l.inserir(1, "funciona")
	assert l[1] == "funciona"
	assert l[2] == "def"
	l.inserir(0, "xpto")
	assert l[0] == "xpto"
	assert len(l) == 5
	l.remover(0)
	assert l[0] == "abc"
	l.remover(1)
	assert l[1] == "def"
	assert len(l) == 3
	l.remover(2)
	assert len(l) == 2
	l.remover(0)
	assert len(l) == 1
	assert l[0] == "def"
	l.remover(0)
	assert l.vazia
	l.inserir(1000, "1")
	l.inserir(1001, "2")
	l.inserir(2, "3")
	assert l[0] == "1"
	assert l[1] == "2"
	assert l[2] == "3"
	l[0] = "r"
	l[1] = "p"
	l[2] = "m"
	assert l[0] == "r"
	assert l[1] == "p"
	assert l[2] == "m"


 

if __name__ == "__main__":
	test_lista_simples()
	test_lista_sequencial()
	test_lista_encadeada()