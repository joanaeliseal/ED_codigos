def soma(a, b):
    return a + soma(b, 1)


print("Alguma coisa")
nome = input("Digite seu nome: ")
print(soma(1, 2))
