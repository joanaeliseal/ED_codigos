from datetime import datetime

class VideoGame:
    contador_numero_serie = 1

    def __init__(self, 
                 data_fabricacao=None, 
                 marca="Sony", 
                 modelo="PS6",
                 capacidade_hd=1024,
                 anos_garantia=1
                 ):
        self.marca = marca
        self.modelo = modelo
        self.data_fabricacao = data_fabricacao if data_fabricacao else datetime.now()
        self.capacidade_hd = capacidade_hd
        self.numero_serie = self.contador_numero_serie
        self.jogos_instalados = ["Spider Men"]
        self.anos_garantia = anos_garantia
        self.incrementa_contador()
        

    def __str__(self) -> str:
        return f"{self.numero_serie} - {self.marca}/{self.modelo}"
    
    @classmethod
    def incrementa_contador(cls):
        cls.contador_numero_serie += 1


v1 = VideoGame()
v2 = VideoGame()
print(v1.numero_serie)
print(v2.numero_serie)
print(v1.data_fabricacao)
v3 = VideoGame(data_fabricacao=datetime(2024, 3, 1))
print(v3.data_fabricacao)
v4 = VideoGame(data_fabricacao=datetime(2024, 2, 29),
               marca="Microsoft",
               modelo="XBox S")
print(v4)

def teste():
    v = VideoGame()

