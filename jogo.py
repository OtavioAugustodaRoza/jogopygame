import pygame

pygame.init()

tm_tela = (800, 600)
tela = pygame.display.set_mode(tm_tela)
pygame.display.set_caption("brick breaker")

tm_bola = 15
bola = pygame.Rect(400 , 400, tm_bola, tm_bola)
tm_jogador = 100
jogador = pygame.Rect(0, 550, tm_jogador, 15)

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
    "preta": (0, 0, 0)
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

    
    if bola.colliderect(jogador):
        movimento_bola[1] = -movimento_bola[1]

    for bloco in blocos[:]:  # iterar sobre cópia para remover
        if bola.colliderect(bloco):
            blocos.remove(bloco)
            movimento_bola[1] = -movimento_bola[1]

    
    if bola.y + tm_bola >= tm_tela[1]:
        return None  

    return movimento_bola


    
def atualizar_pontuacao(potuancao):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render(f'Pontuação: {potuancao}', 1, cores["vermelha"])
    tela.blit(texto, (0, 580))
    if potuancao >= qtde_total_blocos:
        return True
    else:
        return False

blocos = criar_blocos(qtde_blocos_linha, qtde_linhas_blocos)


while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    fim_jogo = atualizar_pontuacao(qtde_total_blocos - len(blocos))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    movimentar_jogador()         
    movimento_bola = movimentar_bola(bola)
    if not movimento_bola:
        fim_jogo = True
  


    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()