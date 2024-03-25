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

    def __repr__(self):
        return f'Jogador({self.__nome})'
