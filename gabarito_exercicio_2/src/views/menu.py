
def menu():

    opts = ["1- Cliente", "2- Produto", "3- Sair"]

    print("="*30)
    print("   === AbacateWare ===   ")
    for opt in opts:
        print(opt)
    print("="*30)
    opt = input("Opção: ")
    return opt


def submenu():

    opts = ["   1- Novo", " 2- Buscar", "   3- Voltar"]

    print("="*30)
    print("   === AbacateWare ===   ")
    for opt in opts:
        print(opt)
    print("="*30)
    opt = input("Opção: ")
    return opt


def cadastra(obj: object):

    for key in obj.__dict__:
        value = input(f"{key}: ")
        setattr(obj, key, value)
    return obj


def busca(obj: object):
    pass
