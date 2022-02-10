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
        self.rect = self.image.get_rect(bottom = 300, left = 80)

        self.jumpSound = pygame.mixer.Sound('audio\jump.mp3')
        self.jumpSound.set_volume(0.5)
    
    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jumpSound.play()
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 0:
            self.frameOne = pygame.image.load('graphics\Fly\Fly1.png').convert_alpha()
            self.frameTwo = pygame.image.load('graphics\Fly\Fly2.png').convert_alpha()
            self.ypos = 210
        else:
            self.frameOne = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
            self.frameTwo = pygame.image.load('graphics\snail\snail2.png').convert_alpha()
            self.ypos = 300

        self.frames = [self.frameOne, self.frameTwo]
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), self.ypos))
    
    def animate(self):
        self.rect.x -= 5
        self.index += 0.1
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]
        
        # self.rect = self.image.get_rect(bottom = self.ypos, x = self.rect.x)
        
        # screen.blit(self.image, self.rect)

    def update(self):
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

def collisions():
    if pygame.sprite.spritecollide(player.sprite, enemyList, False):
        enemyList.empty()
        return True
    else:
        return False

#PyGame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
gameOver = True
font = pygame.font.Font('font\Pixeltype.ttf', 50)

backgroundMusic = pygame.mixer.Sound('audio\music.wav')
backgroundMusic.play(loops = -1)


# Background assets
skySurface = pygame.image.load('graphics\Sky.png').convert()
groundSurface = pygame.image.load('graphics\ground.png').convert()

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
tutorialTextSurface = font.render('Press space to begin', False, 'white')
tutorialTextRect = tutorialTextSurface.get_rect(center = (400, 300))

# Timer
enemyTimer = pygame.USEREVENT + 1
pygame.time.set_timer(enemyTimer, 1500)

player = pygame.sprite.GroupSingle()
player.add(Player())

enemyList = pygame.sprite.Group()

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
                    timeSpent = pygame.time.get_ticks()
                    gameOver = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gameOver == False and playerRect.bottom == 300:
                    playerGravity = -20
                elif gameOver == True:
                    playerRect.bottom = 300
                    timeSpent = pygame.time.get_ticks()
                    gameOver = False
        elif event.type == enemyTimer and gameOver == False:
            enemyList.add(Enemy(randint(0, 1)))
            
    if gameOver == False:
        screen.blit(skySurface, (0, 0))
        screen.blit(groundSurface, (0, 300))
        displayScore()

        player.draw(screen)
        player.update()

        enemyList.draw(screen)
        enemyList.update()

        gameOver = collisions()

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