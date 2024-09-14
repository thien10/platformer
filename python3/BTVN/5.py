import pygame, sys, random
from pygame import display
from pygame.locals import QUIT

black = (0, 0, 0)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
pygame.display.set_caption('5')
DISPLAYSURF.fill((255, 255, 255))
font = pygame.font.SysFont('Arial', 36)
pygame.display.set_caption("Snake Game")

txt = font.render('Text', True, black)
txt_rect = txt.get_rect()
txt_rect.center = (300, 200)
DISPLAYSURF.blit(txt, txt_rect)

pygame.display.update()