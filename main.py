import pygame 
import random 

pygame.init()

# set display screen size and added caption and icon
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyInvader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player 1
playerImg = pygame.image.load('player1.png')
playerX = 370
playerY = 500
playerX_move = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Invader
invaderImg = pygame.image.load('extraterrestrial.png')
INVADER_X = random.randint(0, 800)
INVADER_Y = random.randint(50, 200)
INVADERX_MOVE = 0

def invader(x, y):
    screen.blit(invaderImg, (x, y))


# Loop for keeping window open until closing. Draws screen and updates screen. 
running = True 
while running:

    screen.fill((218, 60, 34))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    # if key pressed, check whether left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_move = -.4
            if event.key == pygame.K_d:
                playerX_move = .4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_move = 0
    
    playerX += playerX_move

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    player(playerX, playerY)
    invader(INVADER_X, INVADER_Y)
    pygame.display.update()


