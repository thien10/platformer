import pygame, sys, random
from pygame.locals import QUIT

pygame.init()

colors = [
  (255, 0, 0),
  (0, 255, 0),
  (0, 0, 255),
  (255, 255, 0),
  (255, 0, 255),
  (0, 255, 255),
]

bg = (255, 255, 255)

screen_x = 600
screen_y = 400
DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y))
DISPLAYSURF.fill(bg)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
       pygame.quit()
       sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        pygame.draw.rect(DISPLAYSURF, random.choice(colors), (random.randint(0, screen_x), random.randint(0, screen_y), 50, 50))
  pygame.display.update()