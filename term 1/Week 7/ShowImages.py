import pygame
pygame.init()

screen = pygame.display.set_mode([1000,750])

vaultBoy = pygame.image.load("vaultboy.png")

for y in range(100, 501, 200): 
    for x in range(100,500,150):
        screen.blit(vaultBoy, [x,y])
        
pygame.display.flip()
