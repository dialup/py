width = int(input("Digite a largura: "))
height = int(input("Digite a altura: "))

for _ in range(0, height):
    for _ in range(0, width):
        print("#", end="")
    print("\n", end="")
