y = int(input("Digite um numero: "))
x = int(input("Digite um numero: "))
linha = 1
coluna = 1
while linha <= x:
    while coluna <= y:
        print(linha * coluna, end="\t")
        coluna += 1
    linha += 1
    print()
    coluna = 1

