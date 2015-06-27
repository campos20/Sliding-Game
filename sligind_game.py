""" python sliding_game.py m=5 n=5

    e: embaralha.

    Criado por: Alexandre Campos
    Criacao:            25/06/2015
    Ultima modificacao: 27/06/2015
"""

# Definicao de cores
PRETO       =   0,   0,   0
BRANCO      = 255, 255, 255
VERMELHO    = 255,   0,   0
VERDE       =   0, 150,   0
AZUL        =   0,   0, 255
CINZAC      = 220, 220, 220
CINZA       = 150, 150, 150
AMARELO     = 255, 255,   0

LARGURA = 100 # Largura de cada peca
DELAY = 8 #tempo de movimento da peca

def main():

    import sys, pygame
    from random import randint

    def mover( s_l, s_c, l, c, delay = DELAY ):
        """Uso: mover(linha, coluna, linha_destino, coluna, destino, tempo = DELAY) Mostra o movimento da peca."""

        if 0 <= s_l+l < m and 0 <= s_c+c <n:

            t=.0

            while t<delay:

                mostrar(s_l+l, s_c+c) # Desenha o tabuleiro menos a peca destino.

                # Peca em movimento
                x = s_l+l-t/delay*l
                y = s_c+c-t/delay*c

                pygame.draw.rect(screen, VERDE, [LARGURA*y, LARGURA*x, LARGURA, LARGURA])
                pygame.draw.rect(screen, BRANCO, [LARGURA*y, LARGURA*x, LARGURA, LARGURA], 1)

                nros = fonte.render( str( matriz[s_l+l][s_c+c] ), True, PRETO)
                a, b = nros.get_size()

                screen.blit(nros, [LARGURA*y + (LARGURA-a)/2, LARGURA*x + (LARGURA-b)/2])

                t += 1

                pygame.display.flip()
                pygame.time.Clock().tick(60)
        
            matriz[s_l][s_c], matriz[s_l+l][s_c+c] = matriz[s_l+l][s_c+c], matriz[s_l][s_c]
            selecao[0] += l
            selecao[1] += c

    def mostrar( omite_linha = None, omite_coluna = None ):

        screen.fill(BRANCO) # Limpa tela

        for i in xrange(m):
            for j in xrange(n):
                if (i != omite_linha or j != omite_coluna) and matriz [i][j] != 0:
                    desenha(i, j)

    def embaralha():
        for i in xrange( 4*m*n ):

            l = [-1, 1][randint(0, 1)] # Movimento randomico
            c = [-1, 1][randint(0, 1)]

            mover( selecao[0], selecao[1], 0, c, 2 )
            mover( selecao[0], selecao[1], l, 0, 2 )

    def desenha(i, j):
        pygame.draw.rect(screen, VERDE, [LARGURA*j, LARGURA*i, LARGURA, LARGURA])
        pygame.draw.rect(screen, BRANCO, [LARGURA*j, LARGURA*i, LARGURA, LARGURA], 1)

        nros = fonte.render( str( matriz[i][j] ), True, PRETO)
        a, b = nros.get_size()
    
        screen.blit(nros, [LARGURA*j + (LARGURA-a)/2, LARGURA*i + (LARGURA-b)/2])

    # Execute python sliding.py m n
    try: m=int(sys.argv[1])
    except: m=4

    try: n=int(sys.argv[2])
    except: n=4

    m = max(2, m) # Tamanho minimo: 2s_l
    n = max(2, n)

    # Tela
    screen = pygame.display.set_mode( ( n*LARGURA, m*LARGURA ) )
    pygame.display.set_caption("Sliding")

    concluido = False

    pygame.init()

    fonte = pygame.font.SysFont('Arial', 40, True) # Textos

    matriz = [[(m-i-1)*n+j for j in xrange(n)] for i in xrange(m)]

    # Espaco vazio inicial
    selecao = [m-1, 0]

    mostrar()
    embaralha()

    while not concluido:

        for Event in pygame.event.get():

            if Event.type == pygame.QUIT: # Fecha o programa
                concluido = True
                break

            elif Event.type == pygame.KEYDOWN: # Botao pressionado

                l, c = 0, 0

                # Seta
                if Event.key == pygame.K_DOWN: # Baixo
                    l=-1

                elif Event.key == pygame.K_UP: # Cima
                    l=1

                elif Event.key == pygame.K_LEFT: # Esquerda
                    c=1

                elif Event.key == pygame.K_RIGHT: # Direita
                    c=-1
                    
                elif Event.key == pygame.K_e:
                    embaralha()


                if l != 0 or c != 0:
                    mover(selecao[0], selecao[1], l, c)

        # Exibe os elementos na tela
        mostrar()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
