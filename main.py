import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

testSurface = pygame.Surface((100, 200))
testSurface.fill('blue')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break
    
    screen.blit(testSurface, (0, 0))

    pygame.display.update()
    clock.tick(60)