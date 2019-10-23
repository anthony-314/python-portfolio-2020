import pygame
from spriteSheetToList import *

class Player:
    def __init__(self,width, height):
        self.speed = 5
        self.image = pygame.image.load("chargas.png").convert_alpha()
        self.image = spriteSheetToList(self.image, 31)
        self.icon = pygame.transform.scale(self.image[0], (32, 32))                                           
        self.rect = self.image[0].get_rect()
        self.mask = pygame.mask.from_surface(self.image[0])

        self.rect.midbottom = [width//2, height]
        self.count = 0
        self.updateCount = 0
        self.screenWidth = width
        self.health = 3

    def draw(self, screen):
        screen.blit(self.image[self.count%len(self.image)], self.rect)
        self.updateCount +=1
        if self.updateCount%5 == 0:
             self.count += 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x-= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left< 0:
            self.rect.left = 0
        if self.rect.right > self.screenWidth:
            self.rect.right = self.screenWidth
        
