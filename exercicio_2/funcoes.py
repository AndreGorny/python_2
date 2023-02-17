def cadastro_cliente():
    cod = input("Código do Cliente: ")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    nascimento = input("Data de Nascimento: ")
    sexo = input("Sexo: ")
    fone = input("Telefone: ")
    endereco = input("Endereço: ")
with open('cliente.csv', 'a') as arquivo:
    arquivo.write(f"{cod}, {nome},"
                  f"{cpf}, {nascimento},"
                  f"{sexo}, {fone},"
                  f"{endereco} \n")