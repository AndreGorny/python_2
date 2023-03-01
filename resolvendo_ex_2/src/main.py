from settings import BASE_DIR
from views.menu import menu, submenu, cadastro
import sys
from model.cliente import Cliente
from model.arquivo import Arquivo

while 1:

    opt = menu()

    if opt == "Sair":
        sys.exit(0)

    action = submenu()

    if opt == "Voltar":
        continue

    if action == "Novo":
        if opt == "Cliente":
            c = Cliente()
            obj = cadastro(c)

        arquivo = Arquivo("cliente.abacate")
        arquivo.escrever(obj)

    if action == "Ler":
        if opt == "Cliente":
            arquivo = Arquivo("cliente.abacate")
            