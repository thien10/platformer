import pygame, sys
from pygame.locals import QUIT

pygame.init()

red = (255, 0, 0)
gray = (149, 189, 189)
green = (0, 255, 0)
d_green = (21, 130, 9)
yellow = (255, 255, 0)
pink = (255, 0, 255)

DISPLAYSURF = pygame.display.set_mode((600, 500))
DISPLAYSURF.fill((0, 255, 255))
pygame.display.set_caption('Bài 1')
while True:
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
    #Nền đất
    pygame.draw.rect(DISPLAYSURF, green, (0, 475, 600, 25))
    #Tường nhà
    pygame.draw.rect(DISPLAYSURF, gray, (150, 175, 300, 300))
    #Mái nhà
    pygame.draw.polygon(DISPLAYSURF, red, ((125, 175), (475, 175), (300, 50)))
    #Mặt trời
    pygame.draw.circle(DISPLAYSURF, yellow, (600, 0), 75)
    pygame.draw.line(DISPLAYSURF, yellow, (495, 0), (515, 0), 15)
    pygame.draw.line(DISPLAYSURF, yellow, (600, 85), (600, 105), 15)
    pygame.draw.line(DISPLAYSURF, yellow, (515, 85), (535, 65), 15)
    #hoa
    pygame.draw.line(DISPLAYSURF, d_green, (75, 425), (75, 475), 10)
    pygame.draw.circle(DISPLAYSURF, pink, (75, 400), 25, 5)
    pygame.draw.circle(DISPLAYSURF, yellow, (75, 400), 10)

    pygame.draw.line(DISPLAYSURF, d_green, (525, 425), (525, 475), 10)
    pygame.draw.circle(DISPLAYSURF, pink, (525, 400), 25, 5)
    pygame.draw.circle(DISPLAYSURF, yellow, (525, 400), 10)
    pygame.display.update()