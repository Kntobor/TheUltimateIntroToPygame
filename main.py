import pygame
from sys import exit

def displayScore():
    currentTime = pygame.time.get_ticks() - timeSpent
    scoreSurface = font.render(f'{int(currentTime / 1000)}', False, 'black')
    scoreRect = scoreSurface.get_rect(center = (400, 30))
    screen.blit(scoreSurface, scoreRect)
timeSpent = 0

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
gameOver = False
font = pygame.font.Font('font\Pixeltype.ttf', 50)

skySurface = pygame.image.load('graphics\Sky.png').convert()
groundSurface = pygame.image.load('graphics\ground.png').convert()

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
                if gameOver == False and playerRect.bottom == 300:
                    playerGravity = -20
                elif gameOver == True:
                    playerRect.bottom = 300
                    snailRect.right = 750
                    timeSpent = pygame.time.get_ticks()
                    gameOver = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gameOver == False and playerRect.bottom == 300:
                    playerGravity = -20
                elif gameOver == True:
                    playerRect.bottom = 300
                    snailRect.right = 750
                    timeSpent = pygame.time.get_ticks
                    gameOver = False
    if gameOver == False:
        screen.blit(skySurface, (0, 0))
        screen.blit(groundSurface, (0, 300))
        displayScore()

        snailRect.left -= 4
        if snailRect.right <= 0:
            snailRect.left = 810
        screen.blit(snailSurface, snailRect)

        playerGravity+= 1
        playerRect.bottom += playerGravity
        if playerRect.bottom >= 300:
            playerRect.bottom = 300
        screen.blit(playerSurface, playerRect)

        if playerRect.colliderect(snailRect):
            gameOver = True
    elif gameOver == True:
        screen.fill('blue')

    pygame.display.update()
    clock.tick(60)