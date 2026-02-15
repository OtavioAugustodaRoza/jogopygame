import pygame

pygame.init()

tm_tela = (800, 600)
tela = pygame.display.set_mode(tm_tela)
pygame.display.set_caption("brick breaker")

tm_bola = 15
bola = pygame.Rect(400 , 400, tm_bola, tm_bola)
tm_jogador = 100
jogador = pygame.Rect(400, 550, tm_jogador, 15)

qtde_blocos_linha = 8
qtde_linhas_blocos= 6
qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos

def criar_blocos(qtde_blocos, qtde_linhas):
    altura = tm_tela[1]
    largura = tm_tela[0]
    distancia_entre_blocos = 5
    largura_bloco = largura / 8 - distancia_entre_blocos
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 10
    blocos = []

    for j in range(qtde_linhas):
        for i in range(qtde_blocos):
            bloco = pygame.Rect(i * (largura_bloco + distancia_entre_blocos) , j * distancia_entre_linhas, largura_bloco, altura_bloco)

            blocos.append(bloco)


    return blocos

cores = {
   "branca": (255, 255, 255),
    "vermelha": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "preta": (0, 0, 0),
    "amarelo": (255, 255, 0)
}

fim_jogo = False
potuancao = 0
movimento_bola = [3,-3]  

def desenhar_inicio_jogo():
   tela.fill(cores["preta"])
   pygame.draw.rect(tela, cores["azul"], jogador)
   pygame.draw.rect(tela, cores["branca"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
         pygame.draw.rect(tela, cores["verde"], bloco)


def movimentar_jogador():
   teclas = pygame.key.get_pressed()
   if teclas[pygame.K_LEFT] and jogador.x > 0:
       jogador.x -= 5
   if teclas[pygame.K_RIGHT] and jogador.x + tm_jogador < tm_tela[0]:
       jogador.x += 5

def movimentar_bola(bola):

    bola.x += movimento_bola[0]
    bola.y += movimento_bola[1]


    if bola.x <= 0 or bola.x + tm_bola >= tm_tela[0]:
        movimento_bola[0] = -movimento_bola[0]


    if bola.y <= 0:
        movimento_bola[1] = -movimento_bola[1]

    # quando a bola bater no teto
    if bola.y + tm_bola >= tm_tela[1]:
        return None    


    if bola.colliderect(jogador):
        movimento_bola[1] = -movimento_bola[1]
        if bola.x > jogador.x + tm_jogador / 2:
            if not movimento_bola[0] == 3:
                movimento_bola[0] = -movimento_bola[0]
        else:
            if not movimento_bola[0] == -3:
                movimento_bola[0] = -movimento_bola[0]
    for bloco in blocos[:]:  # iterar sobre cópia para remover
        if bola.colliderect(bloco):
            blocos.remove(bloco)
            movimento_bola[1] = -movimento_bola[1]


    if bola.y + tm_bola >= tm_tela[1]:
        return False # None tem o mesmo efeito de False
        return False

    return movimento_bola


def atualizar_pontuacao(potuacao):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render(f'Pontuação: {potuacao}', 1, cores["vermelha"])
    tela.blit(texto, (0, 580))
    if potuacao >= qtde_total_blocos:
        return True
    else:
        return False

def menu_morte():
    fonte = pygame.font.SysFont(None, 40)
    texto1 = fonte.render("Você Morreu", 1, cores["vermelha"])
    texto2 = fonte.render("Aperte qualquer botão para continuar", 1, cores["branca"])

    largura1, altura1 = fonte.size("Aperte qualquer botão para continuar")
    largura2, altura2 = fonte.size("Você Morreu")

    posicao_texto2 = (tm_tela[0] / 2 - largura1 / 2, tm_tela[1] / 2)
    posicao_texto1 = (tm_tela[0] / 2 - largura2 / 2, posicao_texto2[1] - 50)


    tela.blit(texto1, posicao_texto1)
    tela.blit(texto2, posicao_texto2)

    pygame.display.flip()

    while True:
        evento = pygame.event.wait()
        if evento.type == pygame.KEYDOWN:
            return True

def tela_vitoria():
    fonte = pygame.font.SysFont(None, 50)
    texto = fonte.render("Parabens você ganhou", 1, cores["amarelo"])
    largura, altura = fonte.size("Parabens você ganhou")
    posicao_texto = (tm_tela[0] / 2 - largura / 2, tm_tela[1] / 2)
    tela.blit(texto, posicao_texto)
    pygame.display.flip()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True
            if evento.type == pygame.KEYDOWN:
                return True



blocos = criar_blocos(qtde_blocos_linha, qtde_linhas_blocos)


while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    if atualizar_pontuacao(qtde_total_blocos - len(blocos)):
        tela_vitoria()
        fim_jogo = True
        continue
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    movimentar_jogador()         
    movimento_bola = movimentar_bola(bola)

    # Sem movimento de bola == Morte
    if not movimento_bola:
        continuar = menu_morte()
        if continuar:
            # Cria os blocos de novo ao morrer
            blocos = criar_blocos(qtde_blocos_linha, qtde_linhas_blocos)

            # Coloca a bola no centro de novo
            bola.x = 400
            bola.y = 400

            # Declara os valores numericos de novo pois movimento_bola vira False ao morrer
            movimento_bola = [3,-3] 


  
    pygame.display.flip()
    pygame.time.wait(10)
