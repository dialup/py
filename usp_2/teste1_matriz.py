def cria_matriz(num_linhas, num_colunas):
    matriz = [] #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite[" + str(i) +"][" + str(j) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz



def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim -1 -i], end=" ")

mat = [[1,2,3], [4,5,6], [7,8,9]]
tarefa(mat)



