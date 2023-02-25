import os
from arquivos import GerArquivos, Arquivo
from usuario import Usuario

BASE_DIR = os.path.dirname(__file__)

a = GerArquivos(
    nome="usuarios.txt",
    modo="r",
    base_dir=os.path.join(BASE_DIR, "apoio")
)
arquivo = a.abrir()

conteudo = Arquivo(arquivo=arquivo)
conteudo = conteudo.ler_linhas()
