class Aluno:
    quantidade = 0

    def __init__(self, nome: str):
        self.nome = nome
        Aluno.incrementar_quantidade()

    def saudacao(self):
        print(f"Olá {self.nome}")

    @classmethod
    def incrementar_quantidade(cls):
        cls.quantidade += 1

    def __str__(self) -> str:
        return f'Aluno "{self.nome}"'


if __name__ == "__main__":
    Aluno.incrementar_quantidade()
    Aluno.incrementar_quantidade()

    rodrigo = Aluno("Rodrigo")
    rodrigo.saudacao()

    maria = Aluno("Maria")
    print(Aluno.quantidade)
