# vim: set fileencoding=utf-8 :
'''

$ > python3 jogo_nim.py

Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato 2

Voce escolheu um campeonato!

**** Rodada 1 ****

Quantas peças? 3
Limite de peças por jogada? 1

Computador começa!

O computador tirou uma peça.
Agora restam 2 peças no tabuleiro.

Quantas peças você vai tirar? 2

Oops! Jogada inválida! Tente de novo.

Quantas peças você vai tirar? 1

Você tirou uma peça.
Agora resta apenas uma peça no tabuleiro.

O computador tirou uma peça.
Fim do jogo! O computador ganhou!

**** Rodada 2 ****

Quantas peças? 3
Limite de peças por jogada? 2

Voce começa!

Quantas peças você vai tirar? 2
Voce tirou 2 peças.
Agora resta apenas uma peça no tabuleiro.

O computador tirou uma peça.
Fim do jogo! O computador ganhou!

**** Rodada 3 ****

Quantas peças? 4
Limite de peças por jogada? 3

Voce começa!

Quantas peças você vai tirar? 2
Voce tirou 2 peças.
Agora restam 2 peças no tabuleiro.

O computador tirou 2 peças.
Fim do jogo! O computador ganhou!

**** Final do campeonato! ****

Placar: Você 0 X 3 Computador '''

def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0:
        for i in range(1, m):
            if n % (m+1) :
                m = m - i
        #if m > 3:
        #    m -= 3
        n = n - m
        print("\n\
        O computador tirou ",m," peça.    \n\
        Agora restam ",n,"peças no tabuleiro.\n")
        return m
    elif n <= m:
        m = n
        n = n - m
        print("\n\
        O computador tirou ",m," peça.\n\
        Agora restam ",n,"peças no tabuleiro.\n")
        return m
    else:
        teste = n % (m + 1)
        m = teste
        n = n - teste
        print("\n\
        O computador tirou ",m," peça.\n\
        Agora restam ",n,"peças no tabuleiro.\n")
        return m

# funcao tera que devolver quantas pecas foram removidas
def usuario_escolhe_jogada(n, m):
    teste = False
    while  teste == False:
        valor = int(input("Quantas peças você vai tirar? "))
        if valor < 1 or valor > m:
            print("\n\
            Oops! Jogada inválida! Tente de novo.")
            teste = False
        else:
            m = valor
            n = n - valor
            print("\n\
            Voce tirou ",m," peça.\n\
            Agora restam ",n,"peças no tabuleiro.\n")
            teste = True
            return m
            teste = True

#if __name__ == "__partida()__":
def partida():
    print("\n\
            Bem-vindo ao jogo do NIM! Escolha:  \n\
                                                \n\
            1 - para jogar uma partida isolada  \n\
            2 - para jogar um campeonato 2 ")
    modo = int(input(""))
    if modo == 1 or modo == 2:
        if modo == 1:
            print("\n\
                Voce escolheu rodada unica!     \n\
                                                \n\
                    **** Rodada unica ****\n ")
            teste = False
            while teste == False:
                n = int(input("Quantas peças? "))
                m = int(input("Limite de peças por jogada? "))
                if n > 0 and n > m:
                    if n % (m + 1) == 0:
                        print("\n\
            Voce começa!\n")
                        usuario_escolhe_jogada(n, m)
                        pecas = n - usuario_escolhe_jogada(n, m)
                        print(pecas)
                        teste = True
                    else:
                        print("\n\
            Computador começa!\n")
                        computador_escolhe_jogada(n, m)
                        pecas = n - computador_escolhe_jogada(n, m)
                        print(pecas)
                        teste = True
                else:
                    teste = False
        elif modo == 2:
            campeonato()
    else:
        return partida()


# funcao que chama *partida() 3 vezes
def campeonato():
    jogos = 0
    print("\n\
            Voce escolheu um campeonato!    \n\
                                                \n\
                **** Rodada 1 ****\n ")
    for i in range():
        partida()
#partida()
