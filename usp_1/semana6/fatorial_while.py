import math

def fatorial(n):
    count = 1
    valor = 1
    while (count <= n):
        valor = valor * count
        count += 1
    print(valor)

n = 1
n = int(input("Digite o valor de n: "))
while n >= 0:
        fatorial(n)
        stop = False
        n = int(input("Digite o valor de n: "))


