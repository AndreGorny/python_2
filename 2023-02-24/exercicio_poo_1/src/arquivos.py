import os
from dataclasses import dataclass
from io import TextIOWrapper


@dataclass
class GerArquivos:
    nome: str
    modo: str = "r"
    base_dir: str = ""

    def abrir(self):
        nome = os.path.join(self.base_dir, self.nome)
        self.arquivo = open(nome, self.modo)
        return self.arquivo

    def fechar(self):
        self.arquivo.close()

    def __del__(self):
        try:
            self.fechar()
        except Exception:
            pass


@dataclass
class Arquivo:
    arquivo: TextIOWrapper

    def ler(self) -> str:
        try:
            return self.arquivo.read()
        except Exception:
            return "Deu pau!"

    def ler_linhas(self) -> list:
        try:
            return self.arquivo.readlines()
        except Exception:
            return []
