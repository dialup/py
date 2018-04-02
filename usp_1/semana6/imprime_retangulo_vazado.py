y = int(input("Digite a largura: "))
x = int(input("Digite a altura: "))
linha = 1
coluna = 1
while coluna <= x:
    while linha <= y:
        if x == coluna:
            print("#", end="")
            linha += 1
        elif y == linha:
            print("#", end="")
            linha += 1
        elif coluna == 1 or coluna == x:
            print("#", end="")
            linha += 1
        elif linha == 1 or linha == y:
            print("#", end="")
            linha += 1
        else:
            print(" ", end="")
            linha += 1
    coluna += 1
    print()
    linha = 1

