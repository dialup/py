def desenhaQuadrado(altura, largura, simbolo = '#', preenchimento = ' '):
    print(simbolo * largura)
    for _ in range(altura-2):
        print('{}{}{}'.format(simbolo, preenchimento * (largura - 2), simbolo))
    print(simbolo * largura)

print('Um quadrado:')
desenhaQuadrado(7, 10)

print('\nOutro quadrado:')
desenhaQuadrado(4, 8, '*', '%')
