print("\n")
texto = input("Digite uma frase para acrescentar ao arquivo:\n")
arquivo = open('teste.txt','a')
arquivo.write(texto + "\n")
print("Operação concluída no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
arquivo.close()

print("\nTexto alterado:")
arquivo = open('teste.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()