from carta import Carta
import random

class Baralho:
    """
    Inicialização cria o atributo cartas e gera 52 cartas p/ baralho
        laço aninhado:
        - laço externo enumera os naipes de 0 a 3
        - laço interno enumera as posições de 1 até 13
    Total de execuções: 52, totalizando as 52 cartas
    Cada iteração cria uma nova instância de Carta com o naipe e posição atuais e a inclui na lista cartas
    """
    def __init__(self):
        self.cartas = []
        for naipe in range(4):
            for posicao in range(1, 14):
                self.cartas.append(Carta(naipe, posicao)) # método append é para listas, não tuplas

    def embaralha(self):
        """ Método que percorre a lista e troca cada carta por outra
        escolhida aleatoriamente. É possível que a carta seja trocada por ela mesma. 
        Para trocar as cartas, usa-se uma atribuição de tupla
        """
        numero_cartas = len(self.cartas)
        for i in range(numero_cartas):
            j = random.raandrange(i, numero_cartas)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]
        # método shuffle serve para embaralhar cartas
            
    def remover_carta(self, carta):
        if carta in self.cartas:
            self.cartas.pop(carta)
            return True
        else:
            return False

    def add_carta(self, posicao, naipe):
        pass

    def esta_vazio(self):
        return (len(self.cartas) == 0)

    def imprimirBaralho(self):
        for carta in self.cartas:
            print(carta)
            #pq nao usar o __str__?
    
    # def __str__(self):
    #     s = ""
    #     for i in range(len(self.cartas)):
    #         s = s + " "*i + str(self.cartas[i]) + "\n"
    #     return s