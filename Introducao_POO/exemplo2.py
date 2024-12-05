class Temporizador:
    
    def __init__(self):
        self.ligado: bool = False
        self.contador: int = 0

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

    def exibir(self, valor: int):
        self.contador = valor

class Lampada:
    
    def __init__(self, cor: str):
        self.ligada: bool = False
        self.cor: str = cor

    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        self.ligada = False

    def estah_ligada(self):
        return self.ligada

class Semaforo:
    
    def __init__(self):
        # atributos/propriedade do objeto Semaforo
        self.temporizador = Temporizador()
        self.lampada_amarela = Lampada("amarela")
        self.lampada_vermelha = Lampada("vermelha")
        self.lampada_verde = Lampada("verde")
        # ----

        self.lampada_verde.ligar()
        self.temporizador.exibir(90)

    def proximo_estado(self):
        if self.lampada_verde.estah_ligada():
            self.lampada_verde.desligar()
            self.lampada_amarela.ligar()
            self.temporizador.exibir(10)
        elif self.lampada_amarela.estah_ligada():
            self.lampada_amarela.desligar()
            self.lampada_vermelha.ligar()
            self.temporizador.exibir(60)
        else:
            self.lampada_vermelha.desligar()
            self.lampada_verde.ligar()
            self.temporizador.exibir(90)

    def get_lampada_acesa(self):
        if self.lampada_verde.estah_ligada():
            return 'verde'
        elif self.lampada_amarela.estah_ligada():
            return 'amarela'
        else:
            return 'vermelha'

    def xyz(self):
        pass






sem = Semaforo()

print(sem.get_lampada_acesa())
sem.proximo_estado()
print(sem.get_lampada_acesa())

