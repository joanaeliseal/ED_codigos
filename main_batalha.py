from carta import Carta
from baralho import Baralho

num_participantes = int(input("Jogadores(máx 4): "))

if 1 <= num_participantes <= 4:
    baralho = Baralho()
    print(f'Barlho: {baralho}')
    num_cartas = len(baralho.cartas) // num_participantes

    for i in range(num_participantes):
        baralho.embaralha()
        print(f"Jogador {i+1}: ")
        for j in range(num_cartas):
            cartas_do_participante = baralho.remover_carta()
            print(f'{cartas_do_participante.imprimirBaralho()}')
else:
    print("Numero de jogadores errado!")
    print("Programa encerrado")