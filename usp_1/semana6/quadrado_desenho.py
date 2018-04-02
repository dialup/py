altura = 5
linha = 1
while linha <= altura:
    print('*', end="")
    coluna = 2
    while coluna < altura:
        if linha ==1 or linha == altura:
            print("*")
        else:
            print(end = " ")
        coluna +=1
    print("*")
    linha += 1


