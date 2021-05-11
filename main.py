import pygame 
import random 

pygame.init()

# set display screen size and added caption and icon
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyInvader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#Background 
background = pygame.image.load("Sunset Lake.jpg")

# Player 1
playerImg = pygame.image.load('player1.png')
playerX = 370
playerY = 500
playerX_move = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Invader
invaderImg = pygame.image.load('ufo (1).png')
INVADER_X = random.randint(0, 736)
INVADER_Y = random.randint(50, 200)
INVADERX_MOVE = 0.15
INVADERY_MOVE = 20

def invader(x, y):
    screen.blit(invaderImg, (x, y))

# Bullet
bulletImg = pygame.image.load('bullets.png')
bulletX = 0
bulletY = 500
bulletY_change = .4
bullet_state = "ready"

def fire_bullet(x,y): 
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))

# Loop for keeping window open until closing. Draws screen and updates screen. 
running = True 
while running:

    # screen.fill((218, 60, 34))
    #background image 
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    # if key pressed, check whether left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_move = -.4
            if event.key == pygame.K_d:
                playerX_move = .4
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_move = 0
    
    # BOUNDARY CHECK PLAYER1
    playerX += playerX_move

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # BOUNDARY CHECK/MOVEMENT OF INVADER 
    INVADER_X += INVADERX_MOVE

    if INVADER_X <= 0:
        INVADERX_MOVE = 0.15
        INVADER_Y += INVADERY_MOVE
    elif INVADER_X >= 736:
        INVADERX_MOVE = -0.15
        INVADER_Y += INVADERY_MOVE

    # Bullet Movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change
    
    player(playerX, playerY)
    invader(INVADER_X, INVADER_Y)
    pygame.display.update()


