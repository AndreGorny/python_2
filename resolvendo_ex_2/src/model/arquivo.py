import os
from dataclasses import dataclass
from gabarito_ex_2 import DATABASE


@dataclass
class GerArquivos:
    nome: str
    modo: str = "r"
    base_dir: str = DATABASE

    def __post_init__(self):
        self.nome_completo = os.path.join(self.base_dir, self.nome)

    def abrir(self):
        self.arquivo = open(self.nome_completo, self.modo)
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
    nome: str
    base_dir: DATABASE
    arquivo: GerArquivos = None

    def __post_init__(self):
        self.arquivo = GerArquivos(
            nome=self.nome,
            base_dir=self.base_dir
        )

    def ler(self) -> str:
        self.arquivo.modo = "r"
        arquivo = self.arquivo.abrir()
        conteudo = arquivo.read()
        self.arquivo.fechar()
        return conteudo

    def escrever(self, obj: object) -> None:
        self.arquivo.modo = "a"
        arquivo = self.arquivo.abrir()
        arquivo.write(str(obj.__dict__))
        self.arquivo.fechar()
