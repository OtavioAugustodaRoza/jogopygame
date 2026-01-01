# Brick Breaker

Um jogo estilo **Brick Breaker** desenvolvido em Python usando a biblioteca **Pygame**.

---

## 🎮 Sobre o Jogo

O objetivo do jogo é destruir todos os blocos verdes com a bola, sem deixar que ela caia fora da tela. O jogador controla a barra azul na parte inferior para rebater a bola.

---

## 🕹 Como Jogar

- **Mover o jogador**:  
  - Tecla **←**: mover para a esquerda  
  - Tecla **→**: mover para a direita
- **Objetivo**: destruir todos os blocos verdes.  
- **Fim de jogo**:  
  - A bola cai fora da tela (perde)  
  - Todos os blocos são destruídos (vence)  

---

## 📦 Estrutura do Projeto

- **main.py**: arquivo principal do jogo  
- **Funções principais**:  
  - `criar_blocos(qtde_blocos, qtde_linhas)`: cria os blocos do jogo  
  - `desenhar_inicio_jogo()`: desenha o jogador e a bola  
  - `desenhar_blocos(blocos)`: desenha todos os blocos  
  - `movimentar_jogador()`: movimenta o jogador com as setas  
  - `movimentar_bola(bola)`: movimenta a bola e trata colisões  
  - `atualizar_pontuacao(pontuacao)`: exibe a pontuação na tela  

---

## 🎨 Cores usadas

- **Preto**: fundo da tela  
- **Azul**: jogador  
- **Branco**: bola  
- **Verde**: blocos  
- **Vermelho**: pontuação  

---

## ⚡ Dependências

- Python 3.x  
- Pygame  

### Instalação do Pygame

```bash
pip install pygame
