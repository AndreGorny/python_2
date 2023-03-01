import sys
from models.arquivo import Arquivo

# from settings import BASE_DIR
from models.cliente import Cliente
from models.produto import Produto
from views.menu import menu, submenu, cadastra

while 1:
    opt = menu()

    if opt == "3" or opt == "Sair":
        sys.exit(0)

    action = submenu()

    if action == "3":
        continue

    if action == "1":
        if opt == "1":
            c = Cliente()
            obj = cadastra(c)
            arquivo = Arquivo("cliente.abacate")
        if opt == "2":
            p = Produto()
            obj = cadastra(p)
            arquivo = Arquivo("produto.abacate")

        arquivo.escrever(obj)

    if action == "2":
        if opt == "1":
            arquivo = Arquivo("cliente.abacate")
            conteudo = arquivo.ler()
            print(conteudo)
        if opt == "2":
            arquivo = Arquivo("produto.abacate")
            conteudo = arquivo.ler()
            print(conteudo)
