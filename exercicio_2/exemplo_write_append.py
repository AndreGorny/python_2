cod = input("Código do Cliente: ")
nome = input("Nome: ")
cpf = input("CPF: ")
nascimento = input("Data de Nascimento: ")
sexo = input("Sexo: ")
fone = input("Telefone: ")
endereco = input("Endereço: ")
with open('cliente.csv', 'a') as arquivo:
    arquivo.write(f"{cod}, {nome},
                  {cpf}, {nascimento},
                  {sexo}, {fone},
                  {endereco}")
#print("Operação concluída no arquivo " + arquivo.name)
