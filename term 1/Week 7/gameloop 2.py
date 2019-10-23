import pygame, sys
pygame.init()

size=width, height = 800, 600
screen= pygame.display.set_mode(size)
black = 0,0,0
vaultBoy = pygame.image.load("vaultboy.png")
vaultBoyRect = vaultBoy.get_rect()
clock = pygame.time.Clock()
FPS = 60
speed = 5

pygame.key.set_repeat(10,10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##               vaultBoyRect = vaultBoyRect.move([-speed,0])
##            if event.key == pygame.K_RIGHT:
##                 vaultBoyRect = vaultBoyRect.move([speed,0])
##            if event.key == pygame.K_UP:
##                vaultBoyRect = vaultBoyRect.move([0,-speed])
##            if event.key == pygame.K_DOWN:
##                 vaultBoyRect = vaultBoyRect.move([0,speed])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        vaultBoyRect = vaultBoyRect.move([-speed,0])
    if keys[pygame.K_RIGHT]:
        vaultBoyRect = vaultBoyRect.move([speed,0])
    if keys[pygame.K_UP]:
        vaultBoyRect = vaultBoyRect.move([0,-speed])
    if keys[pygame.K_DOWN]:
        vaultBoyRect = vaultBoyRect.move([0,speed])
    screen.fill(black)
    screen.blit(vaultBoy, vaultBoyRect)
    clock.tick(FPS)
    pygame.display.flip()
