from enum import Enum
from random import shuffle

class Naipe(Enum):
    OUROS = 1
    PAUS = 2
    ESPADAS = 3
    COPAS = 4


class Carta:
    AS = 1
    VALETE = 11
    DAMA = 12
    REI = 13
    
    def __init__(self, valor: int, naipe: Naipe):
        self.__valor = valor
        self.__naipe = naipe

    def _get_valor_como_string(self):
        match self.__valor:
            case Carta.AS:
                return "Ás"
            case Carta.REI:
                return "Rei"
            case Carta.DAMA:
                return "Dama"
            case Carta.VALETE:
                return "Valete"
            case _:
                return str(self.__valor)
            
    def _get_naipe_como_string(self):
        return self.__naipe.name.title()
        
    def __repr__(self):
        return f'Carta({self._get_valor_como_string()} de {self._get_naipe_como_string()})'
    
    def __eq__(self, outra_carta: 'Carta'): #verifica a igualdade entre objetos
        return self.__valor == outra_carta.__valor
    
    def __gt__(self, outra_carta: 'Carta'): # verifica se uma carta é maior que outra
        return self.__valor > outra_carta.__valor


class Baralho:
    
    def __init__(self):
        self.__cartas = []
        for naipe in Naipe.__members__:
            for valor in range(1, 14):
                self.__cartas.append(Carta(valor, Naipe[naipe]))
        self.embaralhar()

    @property
    def cartas(self):
        return self.__cartas
    
    def embaralhar(self):
        shuffle(self.__cartas)
    
    def __len__(self):
        return len(self.__cartas)
    
    def distribuir(self, jogadores: list['Jogador']):
        total_jogadores = len(jogadores)
        cartas_por_jogador = len(self) // total_jogadores
        for indice, jogador in enumerate(jogadores):
            comeco = indice * cartas_por_jogador
            fim = comeco + cartas_por_jogador
            jogador.receber_cartas(self.cartas[comeco: fim])


class Jogador:

    def __init__(self, nome):
        self.__nome = nome
        self.__cartas = []

    @property
    def cartas(self):
        return self.__cartas

    def receber_cartas(self, cartas: list[Carta]):
        self.__cartas.extend(cartas)

    def pegar_carta(self) -> Carta:
        return self.__cartas.pop()
    
    def receber_carta(self, carta: Carta):
        self.__cartas.insert(0, carta)

    def __repr__(self):
        return f'Jogador({self.__nome})'
    
    

class Jogo:

    def __init__(self, 
                 nome_jogador_1: str, 
                 nome_jogador_2: str, 
                 num_rodadas=100
                 ):
        self.num_rodadas = num_rodadas
        self.jogador_1 = Jogador(nome_jogador_1)
        self.jogador_2 = Jogador(nome_jogador_2)
        self.__cartas_empate = []
        self.__baralho = Baralho()
        self.__baralho.distribuir([self.jogador_1, self.jogador_2])
        

    def rodada(self):
        vencedor: Jogador | None = None
        carta_1 = self.jogador_1.pegar_carta()
        print(f"Carta do {self.jogador_1} = {carta_1}")
        carta_2 = self.jogador_2.pegar_carta()
        print(f"Carta do {self.jogador_2} = {carta_2}")
        if carta_1 > carta_2:
            vencedor = self.jogador_1
        elif carta_2 > carta_1:
            vencedor = self.jogador_2
        else:
            print("Empate na rodada.")
            self.__cartas_empate.append(carta_1)
            self.__cartas_empate.append(carta_2)
            print(f"Montante do empate: {self.__cartas_empate}")

        if vencedor:
            print(f"Vencedor da rodada: {vencedor}")
            vencedor.receber_carta(carta_1)
            vencedor.receber_carta(carta_2)
            for carta in self.__cartas_empate:
                vencedor.receber_carta(carta)
            self.__cartas_empate = []
            self._mostrar_placar()

        return vencedor
    
    def jogar(self):
        rodada_atual = 1
        campeao = None

        while rodada_atual <= self.num_rodadas:
            print(f"Rodada #{rodada_atual}")
            self.rodada()
            rodada_atual += 1
            if not self.jogador_1.cartas:
                break
            if not self.jogador_2.cartas:
                break

        if len(self.jogador_1.cartas) > len(self.jogador_2.cartas):
            campeao = self.jogador_1
        elif len(self.jogador_2.cartas) > len(self.jogador_1.cartas):
            campeao = self.jogador_2

        if campeao:
            print(f"O campeão da jogo foi o {campeao}")
        else:
            print("O jogo terminou em empate.")

        self._mostrar_placar()

    def _mostrar_placar(self):
        print(f"Cartas do {self.jogador_1} = {len(self.jogador_1.cartas)}")
        print(f"Cartas do {self.jogador_2} = {len(self.jogador_2.cartas)}")


        
if __name__ == "__main__":
    jogo = Jogo(
        nome_jogador_1=input("Informe o nome do jogador_1: "),
        nome_jogador_2=input("Informe o nome do jogador_2: "),
        num_rodadas=int(input("Informe o número de rodadas: "))
    )
    jogo.jogar()

