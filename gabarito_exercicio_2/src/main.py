import sys
from models.arquivo import Arquivo

from settings import BASE_DIR
from models.cliente import Cliente
from models.produto import Produto
from views.menu import menu, submenu, cadastra

while 1:
    opt = menu()

    if opt == "Sair":
        sys.exit(0)

    action = submenu()

    if action == "Voltar":
        continue

    if action == "Novo":
        if opt == "Cliente":
            c = Cliente()
            obj = cadastra(c)
            arquivo = Arquivo("cliente.abacate")
        if opt == "Produto":
            p = Produto()
            obj = cadastra(p)
            arquivo = Arquivo("produto.abacate")

        arquivo.escrever(obj)

    if action == "Ler":
        if opt == "Cliente":
            arquivo = Arquivo("cliente.abacate")
            conteudo = arquivo.ler()
            print(conteudo)