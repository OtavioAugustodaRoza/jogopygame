import pygame

pygame.init()

tm_tela = (800, 600)
tela = pygame.display.set_mode(tm_tela)
pygame.display.set_caption("brick breaker")

tm_bola = 15
bola = pygame.rect(400 , 300, tm_bola, tm_bola)
tm_jogador = 100
jogador = pygame.rect(0, 750, tm_jogador, 15)

qtde_blocos_linha = 8
qtde_linhas_blocos= 5
qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos

def criar_blocos(qtde_blocos_linha, qtde_linhas_blocos):
    blocos = []

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
movimento_bola = [1,1]  



tela.fill(cores["preta"])


while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

pygame.time.wait(1)
pygame.display.flip()

pygame.quit()