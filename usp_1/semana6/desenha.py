def desenha(linha):
    while linha > 0:
        coluna = 1
        while coluna <= linha:
            print('*', end='\tab'  )
            coluna += 1
        print()
        linha -= 1

x = 2
count = 0
while x >=0:
    y=0
    while y <= 4:
        print(y)
        y -= 1
    x -= 1
