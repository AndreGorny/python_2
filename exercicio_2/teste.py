def area(larg, comp):
    a = larg * comp
    print(f'As medidas desse terreno são de {larg}m x {comp}m. '
          f'A área desse terreno é de {a}m².')


l1 = float(input('Insira a medida da largura (em metros): '))
l2 = float(input("Insira a medida do comprimento (em metros): "))

area(l1, l2)
