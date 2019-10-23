import pygame, sys
pygame.init()

class Bullet3:
    def __init__(self,image):
        self.speed = [2,2]
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def move(self):
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
size = width, height = 640,480
screen = pygame.display.set_mode(size)
black = 0,0,0

bullet3 = Bullet3 ("bullet3.png")
bullet3s = []
bullet3s.append(bullet3)

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame. KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet3 = Bullet3("bullet3.png")
                bullet3s.append(bullet3)

    for bullet3 in bullet3s:
        bullet3.move()

    screen.fill(black)

    for bullet3 in bullet3s:
        bullet3.draw(screen) 

    clock.tick(FPS)
    pygame.display.flip()



























        
