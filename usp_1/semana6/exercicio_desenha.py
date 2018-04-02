
altura = int(input("Digite a largura: "))
linha = int(input("Digite a altura: "))
x = 0
while linha >= x:
    x += 1
    y = 1
    while altura >= y:
        print("#",end="\a")
        y += 1
    if x == linha:
        print("")
    else:
        print(end = "\n")
