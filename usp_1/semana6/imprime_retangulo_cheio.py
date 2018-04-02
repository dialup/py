y = int(input("Digite a largura: "))
x = int(input("Digite a altura: "))
linha = 1
coluna = 1
while linha <= x:
    while coluna <= y:
        print("#", end="")
        coluna += 1
    linha += 1
    print()
    coluna = 1

