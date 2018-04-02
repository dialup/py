
def multiplica(a, b):
    return a * b

print(multiplica(4,5))

def troca(x, y):
    aux = x
    x = y
    y = aux

x = 10
y = 20

troca(x,y)
print("x =", x, "e y=", y)


def total(x, y, z):
#    return sum(len(x,y,z))
    return len(x) + len(y) + len(z)

def leitura():
    x = -1
    while x > 0:
        x = int(input("VAlor: "))
    return x

