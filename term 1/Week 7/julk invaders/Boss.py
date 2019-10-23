import pygame, random

from spriteSheetToList import *

class Boss:
    def __init__(self, x, y, height):
        self.screenHeight = height
        self.speed = 10
        self.image = pygame.image.load("boss.png").convert_alpha()
        self.image = spriteSheetToList(self.image, 16)
        self.mask = pygame.mask.from_surface(self.image[0])
        self.rect = self.image[0].get_rect()

        self.rect.topleft = [x, y]
        self.count = 0
        self.updateCount = 0
        self.fireRate = 500 
        self.pointValue = 1000
        self.health = 20
        self.ySpeed = 20
        
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
        if self.rect.y <= 0 or self.rect.bottom> self.screenHeight // 2:
            self.ySpeed = -self.ySpeed
        self.rect.y += self.ySpeed

    def willFire(self):
        num = random.randint(1, 20)
        return num == 1
