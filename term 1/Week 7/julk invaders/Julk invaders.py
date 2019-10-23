import pygame, sys, random
from Player import *
from PlayerBullet import *
from Enemy import *
from EnemyBullet import *
from Boss import *
from PowerUp import *

def spawn():
    if wave%10 == 0:
        enemy = Boss(10,10,height)
        enemies.append(enemy)
    elif wave%5 == 0:
        picture = "Enemy.png"
        columns = 7
        for y in range(50, 500, 150):
            for x in range(50, 850, 150):
                enemy = Enemy(x,y,wave,picture,columns)
                enemies.append(enemy )
        
    elif wave%2 == 1:
        picture = "curtn.png"
        columns =3
        for y in range(50, 500, 150):
            for x in range(50, 850, 150):
                enemy = Enemy(x,y,wave,picture,columns)
                enemies.append(enemy)
    elif wave%2 == 0:
        picture = "sone.png"
        columns = 4
        for y in range(50, 500, 150):
            for x in range(50, 850, 150):
                enemy = Enemy(x,y,wave,picture,columns)
                enemies.append(enemy)
                
def getHighScore():
    file = open ("highscores.txt", "r")
    line = file.readline()
    high = 0
    while line !="":
        if int(line) > high:
            high = int (line)
        line = file.readline()
    return high
                            


### INITIALIZE PHAZE
pygame.init()
pygame.display.set_caption("Julk Invaders")

clock = pygame.time.Clock()
FPS = 60

size = width, height = 1650, 950
screen = pygame.display.set_mode(size)

background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, size) 

score = 0
highScore = getHighScore() 
wave = 1
blue = 52,62,79
white = 255,255,255
myFont = pygame.font.SysFont("impact",30)
highScoreLabel = myFont.render("HIGHSCORE:" + str (highScore),False, white)

# this is where we create our game objects
player= Player(width, height)
enemies = []

spawn()

Pbullets = []
Ebullets = []
pUps = []
limit = 10
endTime = 0
timer = False


                           
### GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(Pbullets) <= limit:
                bullet = PlayerBullet((player.rect.centerx - 45, player.rect.centery))
                Pbullets.append(bullet)
                bullet = PlayerBullet((player.rect.centerx + 45, player.rect.centery))
                Pbullets.append(bullet)

                
    if player.health <= 0:
        file = open("highscores.txt","a")
        file.write(str(score)+"\n")
        file.close()
        pygame.quit()
        sys.exit()

    if len(enemies) == 0:
        wave+= 1
        spawn()
        Pbullets = []
        Ebullets = []
        player.health+=1
        
    num = random.randint(1, 2000)
    if num  == 1:
       randX = random.randint(0, width - 32)
       pUp = PowerUp(randX, "dios")
       pUps.append(pUp)
       
    ### Move/ user input Phase
    remove = False
    for pUp in pUps:
        pUp.update()
        if pUp.collision(player):
            if pUp.pType == "dios":
                endtime = pygame.time.get_ticks() + 3000
                limit = 100
                player.speed = 10
                timer = True
                remove = True
        if pUp.delete (height) or remove:
            remove = False
            pUps.remove(pUp)
    if(timer and pygame.time.get_ticks() >= endtime):
        limit = 10
        player.speed = 5 
        timer = False

    
    player.update()            
    for enemy in enemies:
        enemy.fireRate = len(enemies) * 15
        enemy.update()
        if enemy.collision(player):
            player.health = 0
        if enemy.willFire():
            bullet = EnemyBullet(enemy.rect.center)
            Ebullets.append(bullet)

        
    for enemy in enemies:
        if enemy.isCollision(width):
            for enemy in enemies:
                enemy.shiftDown()
            break
        if enemy.limit(height):
            player.health = 0
    remove = False
    for bullet in Ebullets:
        bullet.update()
        if bullet.collision(player):
            player.health -= 1
            remove = True
        if bullet.delete(height) or remove:
            remove = False
            Ebullets.remove(bullet)
        
    remove = False
    for bullet in Pbullets:
        bullet.update()
        for enemy in enemies:
            if bullet.collision(enemy):
                enemy.health -= 1
                if enemy.health <= 0:
                   score += enemy.pointValue
                   enemies.remove(enemy)
                remove = True
        if bullet.delete() or remove:
            remove = False
        
            Pbullets.remove(bullet)
    
    scoreLabel = myFont.render("SCORE:" + str (score), False, white)
    waveLabel = myFont.render("WAVE:" + str (wave), False , white)
    ### DRAW phase
    screen.blit(background, (0,0))

    for bullet in Pbullets + Ebullets + pUps:
        bullet.draw(screen)

    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    screen.blit(scoreLabel, (10,10))
    screen.blit(waveLabel, (10,40))
    screen.blit(highScoreLabel, (10, 70))

    for x in range(60, 60+42 * player.health, 42):
       screen.blit(player.icon, (width - x, 10))
        
    clock.tick(FPS)
    pygame.display.flip()
    
