class Veiculo:

    def __init__(self, cor, modelo, marca, ano) -> None:
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def set_cor(self, cor):
        self.cor = cor


class Carro(Veiculo):
    
    def __init__(self, cor, modelo, marca, ano, limp_para) -> None:
        super().__init__(cor, modelo, marca, ano)
        self.limp_para = limp_para


class Hatch(Carro):

    def __init__(self, cor, modelo, marca, ano, limp_para) -> None:
        super().__init__(cor, modelo, marca, ano, limp_para)


class Moto(Veiculo):

    def __init__(self, cor, modelo, marca, ano, apoio) -> None:
        super().__init__(cor, modelo, marca, ano, apoio)
