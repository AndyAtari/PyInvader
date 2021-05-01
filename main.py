import pygame 

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

def player():
    screen.blit(playerImg, (playerX, playerY))


# Loop for keeping window open until closing. Draws screen and updates screen. 
running = True 
while running:

    screen.fill((221, 160, 221))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    
    
    player()
    pygame.display.update()


# <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-buddha" title="Pixel Buddha">Pixel Buddha</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div> 
