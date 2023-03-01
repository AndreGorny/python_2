class Pessoa:

    def __init__(self,
                 nome: str,
                 idade: int,
                 peso: float,
                 altura: float) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self):
        pass

    def emagrecer(self):
        pass

    def crescer(self, tamanho: float):
        self.altura += tamanho


p = Pessoa("Fulano", 18, 130, 180)

p.envelhecer()
print(p.idade, p.altura)
