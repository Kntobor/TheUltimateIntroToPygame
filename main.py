import pygame
from sys import exit
from random import randint
round = 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.gravity = 0
        self.walkOne = pygame.image.load('graphics\Player\player_walk_1.png')
        self.walkTwo = pygame.image.load('graphics\Player\player_walk_2.png')
        self.walk = [self.walkOne, self.walkTwo]
        self.index = 0
        self.jump = pygame.image.load('graphics\Player\jump.png')

        self.image = self.walk[self.index]
        self.rect = self.image.get_rect(midbottom = (200, 300))
    
    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def applyGravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animate(self):
        if self.rect.bottom < 300:
            self.image = self.jump
        else:
            self.index += 0.1
            if self.index >= len(self.walk):
                self.index = 0
            self.image = self.walk[int(self.index)]

    def update(self):
        self.playerInput()
        self.applyGravity()
        self.animate()

# Score system
timeSpent = 0
currentTime = 0
def displayScore():
    global currentTime
    if gameOver == False:
        currentTime = pygame.time.get_ticks() - timeSpent
        scoreSurface = font.render(f'{int(currentTime / 1000)}', False, 'black')
    elif gameOver == True:
        scoreSurface = font.render(f'Score: {int(currentTime / 1000)}', False, 'white')
    scoreRect = scoreSurface.get_rect(center = (400, 30))
    screen.blit(scoreSurface, scoreRect)

def enemyMovement(enemyList):
    global timeSpent
    global gameOver
    global round
    if enemyList:
        for rect in enemyList:
            rect.x -= 5
            if rect.colliderect(playerRect):
                timeSpent = pygame.time.get_ticks()
                round += 1 
                enemyList.clear()
                gameOver = True
            if rect.right <= 0:
                enemyList.remove(rect)


def displayEnemies(enemyList):
    if enemyList:
        for rect in enemyList:
            if rect.bottom == 300:
                screen.blit(snailSurface, rect)
            elif rect.bottom == 210:
                screen.blit(flySurface, rect)

def animatePlayer():
    global playerSurface
    global playerIndex

    if playerRect.bottom < 300:
        playerSurface = playerJump
    else:
        playerIndex += 0.1
        if playerIndex >= len(playerWalk):
            playerIndex = 0
        playerSurface = playerWalk[int(playerIndex)]


#PyGame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
gameOver = True
font = pygame.font.Font('font\Pixeltype.ttf', 50)

# Background assets
skySurface = pygame.image.load('graphics\Sky.png').convert()
groundSurface = pygame.image.load('graphics\ground.png').convert()

# Enemies
flySurface = pygame.image.load('graphics\Fly\Fly1.png').convert_alpha()
snailSurface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()

enemyRectList = []

# Player
playerWalkOne = pygame.image.load('graphics\Player\player_walk_1.png')
playerWalkTwo = pygame.image.load('graphics\Player\player_walk_2.png')
playerWalk = [playerWalkOne, playerWalkTwo]
playerIndex = 0
playerJump = pygame.image.load('graphics\Player\jump.png')

playerSurface= playerWalk[playerIndex]
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

# Timer
enemyTimer = pygame.USEREVENT + 1
pygame.time.set_timer(enemyTimer, 1500)

player = pygame.sprite.GroupSingle()
player.add(Player())

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
                    enemyRectList.clear()
                    timeSpent = pygame.time.get_ticks()
                    gameOver = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gameOver == False and playerRect.bottom == 300:
                    playerGravity = -20
                elif gameOver == True:
                    playerRect.bottom = 300
                    enemyRectList.clear()
                    timeSpent = pygame.time.get_ticks()
                    gameOver = False
        elif event.type == enemyTimer and gameOver == False:
            enemyType = randint(1, 2)
            if enemyType == 1:
                enemyRectList.append(snailSurface.get_rect(bottom = 300, right = randint(900, 1100)))
            elif enemyType == 2:
                enemyRectList.append(flySurface.get_rect(bottom = 210, right = randint(900, 1100)))
            
                    
    if gameOver == False:
        screen.blit(skySurface, (0, 0))
        screen.blit(groundSurface, (0, 300))
        displayScore()

        playerGravity+= 1
        playerRect.bottom += playerGravity
        if playerRect.bottom >= 300:
            playerRect.bottom = 300
        animatePlayer()
        screen.blit(playerSurface, playerRect)
        player.draw(screen)
        player.update()

        # Obstacle Movement
        enemyMovement(enemyRectList)
        displayEnemies(enemyRectList)

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