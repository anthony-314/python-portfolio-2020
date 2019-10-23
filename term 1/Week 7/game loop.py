import pygame
pygame.init()

# initialization
size = width, height = 500,488
black = 0,0,0
screen = pygame.display.set_mode(size)
vaultBoy = pygame.image.load("vaultboy.png")

vaultBoyRect = vaultBoy.get_rect()
speed = [2,2]


clock = pygame.time.Clock()
FPS = 60

# game loop
while True:
    #move step
    vaultBoyRect = vaultBoyRect.move(speed)
    if vaultBoyRect.left < 0 or vaultBoyRect.right > width:
        speed[0] = -speed[0]
    if vaultBoyRect.top< 0 or vaultBoyRect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(black)
    screen.blit(vaultBoy, vaultBoyRect)

    clock.tick(FPS)
    pygame.display.flip()
