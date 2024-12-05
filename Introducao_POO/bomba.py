from enum import IntEnum

class Display:
    
    def __init__(self, preco_por_litro, total_a_pagar=0.0, litros=0.0):
        self.__preco_por_litro = preco_por_litro
        self.__total_a_pagar = total_a_pagar
        self.__litros = litros

    def set_total_a_pagar(self, valor):
        if valor < 0:
            raise ValueError("Valor não pode ser negativo")
        
        self.__total_a_pagar = valor

    def set_litros(self, valor):
        if valor < 0:
            raise ValueError("Valor não pode ser negativo")
        
        self.__litros = valor

    def exibir(self):
        print(f"Total a pagar: {self.__total_a_pagar}")
        print(f"Litros: {self.__litros:.2f}")
        print(f"Preço por litro: {self.__preco_por_litro}")

    def zerar(self):
        self.__total_a_pagar = 0
        self.__litros = 0


class BombaCombustivel:
    class Tipo(IntEnum):
        GASOLINA =  0
        ALCOOL = 1
        GASOLINA_PREMIUM = 2
    
    def __init__(self, tipo_combustivel: Tipo, preco_por_litro: float):
        self.__tipo_combustivel = tipo_combustivel
        self.__preco_por_litro = preco_por_litro
        self.__display = Display(preco_por_litro)

    def zerar(self):
        self.__display.zerar()

    def abastecer(self, valor: float):
        litros = valor / self.__preco_por_litro
        self.__display.set_litros(litros)
        self.__display.set_total_a_pagar(valor)

    def abastecer_por_litros(self, litros: float):
        self.__display.set_litros(litros)
        total_a_pagar = litros * self.__preco_por_litro
        self.__display.set_total_a_pagar(total_a_pagar)

    def exibir(self):
        print("-"*20)
        print(f"Bomba de {self.__tipo_combustivel.name.title()}")
        self.__display.exibir()
        print("#"*20)





class BombaPosto:
    
    def __init__(self):
        self._bomba_gasolina = BombaCombustivel(BombaCombustivel.Tipo.GASOLINA, 5.89)
        self._bomba_alcool = BombaCombustivel(BombaCombustivel.Tipo.ALCOOL, 4.19)

    def abastecer_gasolina(self, valor):
        self._bomba_gasolina.abastecer(valor)

    def abastecer_alcool(self, valor):
        self._bomba_alcool.abastecer(valor)

    def zerar_alcool(self):
        self._bomba_alcool.zerar()

    def zerar_gasolina(self):
        self._bomba_gasolina.zerar()

    def exibir_gasolina(self):
        self._bomba_gasolina.exibir()

    def exibir_alcool(self):
        self._bomba_alcool.exibir()

    def exibir(self):
        self.exibir_gasolina()
        self.exibir_alcool()
        print()
        print()

    def zerar(self):
        self.zerar_alcool()
        self.zerar_gasolina()


def test():
    b = BombaPosto()
    b.exibir()
    b.abastecer_gasolina(75)
    b.exibir()
    try:
        b.abastecer_alcool(-30)
    except ValueError:
        pass
    b.exibir()
    b.zerar()
    b.exibir()

if __name__ == "__main__":
    test()