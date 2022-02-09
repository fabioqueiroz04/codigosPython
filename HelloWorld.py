import pygame, sys
from pygame.locals import *

#inicia o pygame
pygame.init()

#inicia a janela
windowSurface = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption('Hello world!')

#inicia as cores utilizadas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#inicia as fontes
basicFont = pygame.font.SysFont(None, 48)

#inicia o texto
text = basicFont.render('Hello world!', True, RED, GREEN)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#desenha o fundo branco
windowSurface.fill(YELLOW)

#desenha um poligono verde na superficie
#pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291,106), (236,277), (56, 277), (0,106)))

#desenha algumas linhas azuis na superficie
#pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
#pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
#pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

#desenha um circulo azul na superficie
#pygame.draw.circle(windowSurface, RED, (300, 50), 50, 0)

#desenha uma elipse vermelha na superficie
#pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

#desenha o retangulo do fundo do texto na superficie
pygame.draw.rect(windowSurface, WHITE, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

#obtem um array de pixel na superficie
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380]=RED
del pixArray

#desenha o texto na janela
windowSurface.blit(text, textRect)

#desenha a janela na tela
pygame.display.update()

#roda o loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()