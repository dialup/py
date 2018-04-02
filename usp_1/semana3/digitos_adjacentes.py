n = int(input("Digite um numero: "))
sim = 0
while(n // 10 != 0):
    teste_a = n % 10
    n = n // 10
    teste_b = n % 10
    if teste_a == teste_b or teste_b == teste_a:
        sim += 1
if sim != 0:
    print("sim")
else:
    print("não")
