
def menu():

    opts = ["Cliente", "Produto", "Sair"]

    print("="*30)
    print("   === AbacateWare ===   ")
    for opt in opts:
        print(opt)
    print("="*30)
    opt = input("Opção: ")
    return opt

def submenu():

    opts = ["Novo", "Buscar", "Voltar"]

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