class Carta:
    def __init__(self, naipe=0, posicao=0):
        """
        Espadas: 3        Valete: 11
        Copas: 2          Rainha: 12
        Ouros: 1          Rei: 13
        Paus: 0

        - mapeamento entre uma sequencia de números e os itens que eu quero representar
        - naipes mapeados com números inteiros
        - posições mapeadas de acordo com o valor da carta
        """
        self.__naipe = naipe
        self.__posicao = posicao

    listaDeNaipes = ["Paus", "Ouros", "Copas", "Espadas"]
    listaDePosicoes = ["0", "Ás", "2", "3", "4",
                       "5", "6", "7", "8", "9", "10",
                       "Valete", "Rainha", "Rei"]
    
    def getNaipe(self):
        return self.__naipe
    
    def getPosicao(self):
        return self.__posicao  
    
    # def __gt__(self, posicao):
    #     """rich comparison: chamado pelo operador >"""
    #     pass

    # def __lt__(self, posicao):
    #     """rich comparison: chamado pelo operador <"""
    #     pass
    
    def __cmp__(self, other):
        # verificar os naipes
        if self.__naipe > other.__naipe: return 1
        if self.__naipe < other.__naipe: return -1
        # as cartas têm o mesmo naipe... verificar as posições
        if self.__posicao > other.__posicao: return 1
        if self.__posicao < other.__posicao: return -1
        # as posições são iguais... é um empate
        return 0
    
    def __str__(self):
        return f"{self.__posicao} de {self.__naipe}"
    