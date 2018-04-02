#coding: utf-8
'''
Δ < 0, então a equação não possui resultados reais;

Δ = 0, então a equação possui apenas um resultado real ou possui
    dois resultados iguais (essas duas afirmações são equivalentes);

Δ > 0, então a equação possui dois resultados distintos reais.
'''

import math
a= float(input("Digite a:"))
b= float(input("Digite b:"))
c= float(input("Digite c:"))

delta = b**2-4*a*c
if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) /  (2 * a)
    print("a raiz desta equação é",raiz1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) /  (2 * a)
        raiz2 = (-b - math.sqrt(delta)) /  (2 * a)
        if raiz1 < raiz2:
            print("as raízes da equação são",raiz1,"e",raiz2)
        else:
            print("as raízes da equação são",raiz2,"e",raiz1)
