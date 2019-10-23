import pygame, sys, math

def wiggle( xPos ):
    yPos = 100.0 + 50*math.sin(0.0003 * xPos * 180.0 / math.pi)
    return yPos

pygame.init ()
size = width, height =640, 480
black = 0,0,0
screen = pygame.display.set_mode(size)
vaultBoy = pygame.image.load("vaultboy.png")
vaultBoyRect = vaultBoy.get_rect()

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    vaultBoyRect.x += 1
    # vaultBoyRect.x = vaultBoyRect
    vaultBoyRect.y = wiggle (vaultBoyRect.x)

    screen.fill(black)
    screen.blit(vaultBoy, vaultBoyRect)
    clock.tick(FPS)

    pygame.display.flip()
