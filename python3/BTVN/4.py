import pygame, sys, random
from pygame.locals import QUIT

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 500))
DISPLAYSURF.fill((66, 66, 66))

def colors():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return r, g, b

color_change = False



pygame.draw.polygon(DISPLAYSURF, (255, 255, 255), ((200, 150), (300, 150), (250, 50)))
pygame.draw.polygon(DISPLAYSURF, (255, 255, 255), ((200, 350), (300, 350), (250, 450)))
pygame.draw.polygon(DISPLAYSURF, (255, 255, 255), ((150, 200), (150, 300), (50, 250)))
pygame.draw.polygon(DISPLAYSURF, (255, 255, 255), ((350, 200), (350, 300), (450, 250)))

pygame.display.update()
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
       pygame.quit()
       sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        pygame.draw.polygon(DISPLAYSURF, colors(), ((150, 200), (150, 300), (50, 250)))
      elif event.key == pygame.K_RIGHT:
        pygame.draw.polygon(DISPLAYSURF, colors(), ((350, 200), (350, 300), (450, 250)))
      elif event.key == pygame.K_UP:
        pygame.draw.polygon(DISPLAYSURF, colors(), ((200, 150), (300, 150), (250, 50)))
      elif event.key == pygame.K_DOWN:
        pygame.draw.polygon(DISPLAYSURF, colors(), ((200, 350), (300, 350), (250, 450)))
      elif event.key == pygame.K_SPACE:
        pygame.draw.polygon(DISPLAYSURF, colors(), ((200, 150), (300, 150), (250, 50)))
        pygame.draw.polygon(DISPLAYSURF, colors(), ((200, 350), (300, 350), (250, 450)))
        pygame.draw.polygon(DISPLAYSURF, colors(), ((150, 200), (150, 300), (50, 250)))
        pygame.draw.polygon(DISPLAYSURF, colors(), ((350, 200), (350, 300), (450, 250)))
      elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
        if color_change == False:
          color_change = True
        else:
          color_change = False

  if color_change:
    pygame.draw.polygon(DISPLAYSURF, colors(), ((200, 150), (300, 150), (250, 50)))
    pygame.draw.polygon(DISPLAYSURF, colors(), ((200, 350), (300, 350), (250, 450)))
    pygame.draw.polygon(DISPLAYSURF, colors(), ((150, 200), (150, 300), (50, 250)))
    pygame.draw.polygon(DISPLAYSURF, colors(), ((350, 200), (350, 300), (450, 250)))
    pygame.display.update()
          
  pygame.display.update()
