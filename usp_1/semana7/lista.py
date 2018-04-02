
num = []
teste = False 
while teste == False:
    a = int(input("Digite um numero inteiro > 0: "))
    if a == 0:
        print(num)
        teste = True
    else:
        num.append(a)
        teste = False
