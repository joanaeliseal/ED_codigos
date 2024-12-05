
MENU_STRING = """
+--------------+
| {registrador} |
+--------------+
(+) somar
(-) subtrair
(/) dividir
(*) multiplicar
(r) resetar
(d) desfazer
(s) sair
---------------
"""

class Calculadora:

    def __init__(self):
        self.registrador: int = 0
        self.valores = []

    def salvar_registrador(self):
        self.valores.append(self.registrador)

    def adicionar(self, valor: int):
        self.salvar_registrador()
        self.registrador += valor

    def subtrair(self, valor: int):
        self.salvar_registrador()
        self.registrador -= valor

    def dividir(self, valor: int):
        self.salvar_registrador()
        self.registrador /= valor

    def multiplicar(self, valor: int):
        self.salvar_registrador()
        self.registrador *= valor

    def get_registrador(self) -> int:
        return self.registrador
    
    def reset(self):
        self.registrador = 0

    def exibir(self):
        print(self.registrador)

    def desfazer(self):
        if self.valores:
            self.registrador = self.valores.pop()


class InterfaceUsuario:

    def __init__(self):
        self.calculadora = Calculadora()

    def exibir_menu(self):
        print(MENU_STRING.format(
            registrador=self.calculadora.get_registrador())
        )

    def executar(self):
        while True:
            self.exibir_menu()
            operacao = input("Operação:")
            match operacao:
                case "+":
                    valor = int(input("Valor: "))
                    self.calculadora.adicionar(valor)
                case "-":
                    valor = int(input("Valor: "))
                    self.calculadora.subtrair(valor)
                case "*":
                    valor = int(input("Valor: "))
                    self.calculadora.multiplicar(valor)
                case "/":
                    valor = int(input("Valor: "))
                    if valor == 0:
                        print("Divisão impossível")
                    else:
                        self.calculadora.dividir(valor)
                case "r":
                    self.calculadora.reset()
                case "d":
                    self.calculadora.desfazer()
                case "s":
                    print("Encerrando a calculadora...")
                    break
                case _:
                    print("Opção inválida")


if __name__ == "__main__":
    interface = InterfaceUsuario()
    interface.executar()