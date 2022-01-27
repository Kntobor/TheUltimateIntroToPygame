import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #draw and update all elements
    pygame.display.update()