import math

a = int(input("Por favor digite um numero para multiplicar: \n"))
b = 0
c = 0
if a <= 10:
    while c <= 10:
        d = a * b
        print (a,"x",b,"=",d, )
        b += 1
        c += 1
else:
    print("Opa, esse numero e maior que 10")
