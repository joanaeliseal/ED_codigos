class Relogio:

    def __init__(self):
        self.__hora = 0
        self.__minutos = 0
        self.__segundos = 0

    def get_hora_formatada(self):
        return f'{self.__hora:02}:{self.__minutos:02}:{self.__segundos:02}'

    def get_minutos(self):
        return self.__minutos

    def get_segundos(self):
        return self.__segundos

    def get_hora(self):
        return self.__hora
    
    def set_hora(self, h: int):
        if 0 <= h <= 23:
            self.__hora = h

    def set_minutos(self, m: int):
        if 0 <= m <= 59:
            self.__minutos = m

    def set_segundos(self, s: int):
        if 0 <= s <= 59:
            self.__segundos = s

    def adicionar_hora(self, h: int):
        self.__hora = (self.__hora + h) % 24
    
    def adicionar_minutos(self, m: int):
        total_minutos = self.__minutos + m
        self.__minutos = total_minutos % 60
        self.adicionar_hora(total_minutos // 60)

    def adicionar_segundos(self, s: int):
        total_segundos = self.__segundos + s
        self.__segundos = total_segundos % 60
        self.adicionar_minutos(total_segundos // 60)



class Relogio2:

    def __init__(self, total_segundos=0):
        self.__total_segundos = total_segundos

    def get_hora_formatada(self):
        return f'{self.get_hora():02}:{self.get_minutos():02}:{self.get_segundos():02}'
    
    def __repr__(self):
        return self.get_hora_formatada()

    def get_minutos(self):
        h = self.get_hora()
        valor = self.__total_segundos
        if h > 0:
            valor = valor - (h*60*60)
        return valor // 60 

    def get_segundos(self):
        valor = self.__total_segundos
        h = self.get_hora()
        m = self.get_minutos()
        if h > 0:
            valor = valor - (h*60*60)
        if m > 0:
            valor = valor - (m*60)
        return valor

    def get_hora(self):
        return self.__total_segundos // 3600
    
    def set_hora(self, h: int):
        if not 0 <= h <= 23:
            return
    
        if h > self.get_hora():
            diferenca = h - self.get_hora()
            self.__total_segundos += (diferenca * 60 * 60)
        else:
            diferenca = self.get_hora() - h
            self.__total_segundos -= (diferenca * 60 * 60)

    def set_minutos(self, m: int):
        if not 0 <= m <= 59:
            return 
        if m > self.get_minutos():
            diferenca = m - self.get_minutos()
            self.__total_segundos += (diferenca * 60)
        else:
            diferenca = self.get_minutos() - m
            self.__total_segundos -= (diferenca * 60)

    def set_segundos(self, s: int):
        if not 0 <= s <= 59:
            raise ValueError(f"Valor inválido para segundo. {s}") 
        
        if s > self.get_segundos():
            diferenca = s - self.get_segundos()
            self.__total_segundos += diferenca
        else:
            diferenca = self.get_segundos() - s
            self.__total_segundos -= diferenca

    def adicionar_hora(self, h: int):
        self.__total_segundos += h * 60 * 60
    
    def adicionar_minutos(self, m: int):
        self.__total_segundos += m * 60

    def adicionar_segundos(self, s: int):
        self.__total_segundos += s
        