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
                        vencedor = False
                        total = n
                        while vencedor == False:
                            peca = usuario_escolhe_jogada(total, m)
                            total = total - peca
                            print("\n\
            Voce tirou ",peca, " peça.\n\
            Agora restam ",total,"peças no tabuleiro.\n")
                            if total <= 0:
                                print("Voce Ganhou")
                                return
                            computador_escolhe_jogada(total, m)
                            total = total - computador_escolhe_jogada(total, m)
                            print("\n\
            O computador tirou ",computador_escolhe_jogada(n, m)," peça.\n\
            Agora restam ",total,"peças no tabuleiro.\n")
                            if total <= 0:
                                print("Computador Venceu.")
                                return
                                teste = True
                    else:
                        print("\n\
            Computador começa!\n")
                        vencedor = False
                        total = n
                        while vencedor == False:
                            computador_escolhe_jogada(total, m)
                            total = total - computador_escolhe_jogada(total, m)
                            print("\n\
            O computador tirou ",computador_escolhe_jogada(total, m)," peça.\n\
            Agora restam ",total,"peças no tabuleiro.\n")
                            if total <= 0:
                                print("Computador Venceu.")
                                return
                            user = usuario_escolhe_jogada(total, m) 
                            total = total - user
                            print("\n\
            Voce tirou ",user, " peça.\n\
            Agora restam ",total,"peças no tabuleiro.\n")
                            if n <= 0:
                                print("Voce Ganhou")
                                return
                else:
                    teste = False
        elif modo == 2:
            campeonato()
    else:
        return partida()

# funcao que pergunta quem comeca e quantas pecas.
# funcao que vai chamar as outras funcoes
# funcao que vai ficar com lacos para comandar quantas pecas de (n, m)
#   foram retiradas.
# funcao que finaliza o game (n == 0)
# variaveis (n and m) NAO NAO NAO NAO deverao ser globais

#def partida(n, m):

#return True

# funcao tera que devolver quantas pecas foram removidas
def computador_escolhe_jogada(n, m):
    if n <= m:
        m = n
        n = n - m
        return m
    elif n % (m + 1) == 0:
        for i in range(1, m):
            if n % (m+1) :
                m = m - i
        #if m > 3:
        #    m -= 3
        n = n - m
        return m
    else:
        teste = n % (m + 1)
        m = teste
        n = n - m
        return m
#        print("\n\
#        O computador tirou ",m," peça.\n\
#        Agora restam ",n,"peças no tabuleiro.\n")

# funcao tera que devolver quantas pecas foram removidas
def usuario_escolhe_jogada(n, m):
    tt = False
    while tt == False:
        valor = int(input("Quantas peças você vai tirar? "))
        if valor < 1 or valor > m:
            print("\n\
            Oops! Jogada inválida! Tente de novo.")
            tt = False
        elif valor >= 1 or valor < m:
            return valor
            tt = True



# funcao que chama *partida() 3 vezes
def campeonato():
    jogos = 0
    print("\n\
            Voce escolheu um campeonato!    \n\
                                                \n\
                **** Rodada 1 ****\n ")
    partida(n, m)
partida()
