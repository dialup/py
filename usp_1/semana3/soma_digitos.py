n = int(input("digite um numero inteiro: "))
total_t = 0
while(n != 0):
    total = n % 10
    total_t = total_t + total
    n = n // 10
print(total_t)
