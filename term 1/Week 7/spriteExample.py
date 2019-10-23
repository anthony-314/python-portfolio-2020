import pygame
from spriteSheetToList import *

pygame.init()

size = width, height = 640, 480
white = 47,63,89

screen = pygame.display.set_mode(size)

enemy = pygame.image.load("enemy.png").convert_alpha()
enemy = spriteSheeToList(enemy, 4)
enemyRect = enemy[0].get_rect()

clock = pygame.time.Clock()
FPS = 60

count = 0
updateCount = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(white)
    screen.blit(enemy[count%len(enemy)], enemyRect)
    if updateCount%5== 0:
        count += 1
    updateCount +=1
    
    clock.tick(FPS)
    pygame.display.flip()
