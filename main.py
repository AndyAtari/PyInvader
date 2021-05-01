import pygame 

pygame.init()

# set display screen size and added caption and icon
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyInvader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Loop for keeping window open until clicking X. Changes screen color and updates while loop is running. 
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    screen.fill((221, 160, 221))
    pygame.display.update()

# <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-buddha" title="Pixel Buddha">Pixel Buddha</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

