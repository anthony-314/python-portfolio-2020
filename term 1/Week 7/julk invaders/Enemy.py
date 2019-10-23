import pygame, random

from spriteSheetToList import *

class Enemy:
    def __init__(self, x, y, wave, picture, frames):
        self.wave = wave
        self.speed = self.wave + 5
        self.image = pygame.image.load(picture).convert_alpha()
        self.image = spriteSheetToList(self.image, frames)
        self.mask = pygame.mask.from_surface(self.image[0])
        self.rect = self.image[0].get_rect()

        self.rect.topleft = [x, y]
        self.count = 0
        self.updateCount = 0
        self.fireRate = 500 
        self.pointValue = 100
        self.health = 1
        
    def draw(self, screen):
        screen.blit(self.image[self.count%len(self.image)], self.rect)
        self.updateCount +=1
        if self.updateCount%5 == 0:
             self.count += 1
    def update(self):
        self.rect.x += self.speed

    def isCollision(self, width):
        if self.rect.right > width or self.rect.left < 0:
            return True
        else:
            return False

    def collision (self, enemy):
        offsetX = enemy.rect.left - self.rect.left
        offsetY = enemy.rect.top - self.rect.top
        if self.mask.overlap (enemy.mask, (offsetX, offsetY)) !=None:
            return True
        else:
            return False

    def limit(self, height):
        return self.rect.bottom >= height

    def shiftDown(self):
        self.speed = -self.speed
        self.rect.y += 20

    def willFire(self):
        value = self.fireRate - self.wave* 2
        if value <= 10:
            value = 10
        num = random.randint(1, value)
        return num == 1
