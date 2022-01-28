import pygame
from sys import exit
round = 1

# Score System
currentTime = 0
timeSpent = 0
def displayScore():
    global currentTime
    if gameOver == False:
        currentTime = int((pygame.time.get_ticks() - timeSpent )/ 1000)
        scoreSurface = font.render(f'Score: {currentTime}', False, 'black')
    elif gameOver == True:
        scoreSurface = font.render(f'Score: {currentTime}', False, 'white')
    scoreRect = scoreSurface.get_rect(center = (400, 30))
    screen.blit(scoreSurface, scoreRect)

#PyGame Setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
gameOver = True
font = pygame.font.Font('font\Pixeltype.ttf', 50)

# Background Assets
skySurface = pygame.image.load('graphics\Sky.png').convert()
groundSurface = pygame.image.load('graphics\ground.png').convert()

# Enemies
snailSurface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snailRect = snailSurface.get_rect(bottom = 300, right = 750)

# Player
playerSurface = pygame.image.load('graphics\Player\player_walk_1.png')
playerRect = playerSurface.get_rect(bottom = 300, left = 80)
playerGravity = 0

# Menu Screen
menuCharacterSurface = pygame.image.load('graphics\Player\player_stand.png').convert_alpha()
menuCharacterSurface = pygame.transform.scale(menuCharacterSurface, (136, 168))
menuCharacterRect = menuCharacterSurface.get_rect(center = (400, 200))
titleTextSurface = font.render('Runner', False, 'white')
titleTextRect = titleTextSurface.get_rect(center = (400, 30))
tutorialTextSurface = font.render('Click or press space to begin', False, 'white')
tutorialTextRect = tutorialTextSurface.get_rect(center = (400, 300))

# Game Loop
while True:
    # Event Checker
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
            round += 1
            gameOver = True
    elif gameOver == True:
        screen.fill((94, 129, 162))
        screen.blit(menuCharacterSurface, menuCharacterRect)
        if round != 1:
            displayScore()
        elif round == 1:
            screen.blit(titleTextSurface, titleTextRect)
        screen.blit(tutorialTextSurface, tutorialTextRect)

    pygame.display.update()
    clock.tick(60)