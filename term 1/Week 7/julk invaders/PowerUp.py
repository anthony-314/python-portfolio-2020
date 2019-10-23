import pygame
from spriteSheetToList import *

class PowerUp:
    def __init__ (self,x,pType):
        self.pType = pType
        if self.pType == "dios":
            self.image = pygame.image.load(self.pType + ".png").convert_alpha()
            self.image = spriteSheetToList(self.image, 1)

        self.rect = self.image[0].get_rect()
        self.mask = pygame.mask.from_surface(self.image[0])

        self.speed = 2
        self.rect.bottom = 0
        self.rect.x = x

        self.count = 0
        self.updateCount = 0

    def draw(self, screen):
        screen.blit(self.image[self.count%len(self.image)], self.rect)
        self.updateCount +=1
        if self.updateCount%5 == 0:
             self.count += 1

    def update(self):
        self.rect.y += self.speed


    def delete(self, height):
        if self.rect.top > height:
            return True
        else:
            return False
        
    def collision(self, enemy):
        offsetX = enemy.rect.left - self.rect.left
        offsetY = enemy.rect.top - self.rect.top
        if self.mask.overlap(enemy.mask, (offsetX, offsetY)) != None:
            return True
        else:
            return False
