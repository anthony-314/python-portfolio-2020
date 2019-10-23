import pygame, sys

pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
white = 255,255,255

bullet3 = pygame.image.load('bullet3.png')
battle = pygame.image.load('battle.png')


bullet3Rect = bullet3.get_rect()
battleRect = battle.get_rect()

bullet3Mask = pygame.mask.from_surface(bullet3)
battleMask = pygame.mask.from_surface(battle)

pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bullet3Rect.center = pygame.mouse.get_pos()
    offsetX = battleRect.left - bullet3Rect.left
    offsetY = battleRect.top - bullet3Rect.top

    if( bullet3Mask.overlap(battleMask, (offsetX, offsetY)) != None):
        print('collision Detected!')
    else:
            print('None')

    screen.fill(white)
    screen.blit(battle, battleRect)
    screen.blit(bullet3, bullet3Rect)
    pygame.display.flip()
