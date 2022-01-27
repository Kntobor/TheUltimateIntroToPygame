import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

skySurface = pygame.image.load('graphics\Sky.png')
groundSurface = pygame.image.load('graphics\ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break
    
    screen.blit(skySurface, (0, 0))
    screen.blit(groundSurface, (0, 300))

    pygame.display.update()
    clock.tick(60)