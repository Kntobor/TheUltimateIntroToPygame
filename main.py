import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
testFont = pygame.font.Font('font\Pixeltype.ttf', 50)

skySurface = pygame.image.load('graphics\Sky.png').convert()
groundSurface = pygame.image.load('graphics\ground.png').convert()
scoreSurface = testFont.render('0', False, 'black')
scoreRect = scoreSurface.get_rect(center = (400, 30))

snailSurface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snailRect = snailSurface.get_rect(bottom = 300, right = 750)

playerSurface = pygame.image.load('graphics\Player\player_walk_1.png')
playerRect = playerSurface.get_rect(bottom = 300, left = 80)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break
    
    screen.blit(skySurface, (0, 0))
    screen.blit(groundSurface, (0, 300))
    screen.blit(scoreSurface, scoreRect)

    snailRect.left -= 4
    if snailRect.left < -100:
        snailRect.left = 810
    screen.blit(snailSurface, snailRect)
    screen.blit(playerSurface, playerRect)

    pygame.display.update()
    clock.tick(60)