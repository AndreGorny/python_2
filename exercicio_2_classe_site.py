class Quadrado:

    def __init__(self, lado: float) -> None:
        self.lado = lado

    def area(self) -> float:
        return self.lado * self.lado

    def set_lado(self, lado) -> None:
        self.lado = lado

    def get_lado(self) -> float:
        return self.lado


Quadrado.set_lado(4)
Quadrado.get_lado
