import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('font\Pixeltype.ttf', 50)

skySurface = pygame.image.load('graphics\Sky.png').convert()
groundSurface = pygame.image.load('graphics\ground.png').convert()
scoreSurface = font.render('0', False, 'black')
scoreRect = scoreSurface.get_rect(center = (400, 30))

snailSurface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snailRect = snailSurface.get_rect(bottom = 300, right = 750)

playerSurface = pygame.image.load('graphics\Player\player_walk_1.png')
playerRect = playerSurface.get_rect(bottom = 300, left = 80)
playerGravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if playerRect.bottom == 30:
                playerGravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playerRect.bottom == 300:
                    playerGravity = -20
    
    screen.blit(skySurface, (0, 0))
    screen.blit(groundSurface, (0, 300))
    screen.blit(scoreSurface, scoreRect)

    snailRect.left -= 4
    if snailRect.right <= 0:
        snailRect.left = 810
    screen.blit(snailSurface, snailRect)

    #Player
    playerGravity+= 1
    playerRect.bottom += playerGravity
    if playerRect.bottom >= 300:
        playerRect.bottom = 300
    screen.blit(playerSurface, playerRect)

    if playerRect.colliderect(snailRect):
        pygame.quit()
        exit()
        break

    pygame.display.update()
    clock.tick(60)