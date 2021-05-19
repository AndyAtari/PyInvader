import pygame 
import random 
import math

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
invaderImg = []
invaderX = []
invaderY = []
invaderX_move = []
invaderY_move = []
num_of_invaders = 10

# Drawing Invaders 
for i in range(num_of_invaders):

    invaderImg.append(pygame.image.load('ufo (1).png'))
    invaderX.append(random.randint(0, 736))
    invaderY.append(random.randint(50, 200))
    invaderX_move.append(0.2)
    invaderY_move.append(20)

def invader(x, y, i):
    screen.blit(invaderImg[i], (x, y))

# Explosions 

explosionImg = pygame.image.load('explosion2.png')

def explosion(x, y):
    screen.blit(explosionImg, (x, y))

# Bullet
bulletImg = pygame.image.load('bullets.png')
bulletX = 0
bulletY = 500
bulletY_change = .3
bullet_state = "ready"

def fire_bullet(x,y): 
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))

def isCollision(invaderX, invaderY, bulletX, bulletY):
    distance = math.sqrt(math.pow(invaderX - bulletX,2) + math.pow(invaderY - bulletY,2))
    if distance < 32:
        return True
    else:
        return False

# Score 
score = 0
font = pygame.font.Font('neo_scifi.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    score_display = font.render("Score: " + str(score), True, (173, 216, 230))
    screen.blit(score_display, (x, y))

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
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
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
    for i in range(num_of_invaders):
        invaderX[i] += invaderX_move[i]

        if invaderX[i] <= 0:
            invaderX_move[i] = 0.2
            invaderY[i] += invaderY_move[i]
        elif invaderX[i] >= 736:
            invaderX_move[i] = -0.2
            invaderY[i] += invaderY_move[i]

        collision = isCollision(invaderX[i], invaderY[i], bulletX, bulletY)
        if collision:
            explosion(invaderX[i], invaderY[i])
            bulletY = 500
            bullet_state = "ready"
            score += 100
            invaderX[i] = random.randint(0, 736)
            invaderY[i] = random.randint(50, 200)

        invader(invaderX[i], invaderY[i], i)
        

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change  
    
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()


