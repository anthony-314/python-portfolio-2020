import pygame
import random
import math

pygame.init()

def make_random_entity(width, height, x):
    new_x = random.randint(x*180, 180 + 180* x)
    rect = pygame.rect.Rect(new_x, 0, width, height)
    return rect

def make_random_key(width, height):
    new_x = random.randint(0, 1000)
    new_y = random.randint (0, 650)
    rect = pygame.rect.Rect(new_x, new_y, width, height)
    return rect

def load_sprites(number, path, scale_width, scale_height):
    images = []
    for count in range(0, number):
         image = pygame.image.load(path + str(count) + ".png").convert_alpha()
         image = pygame.transform.scale(image, (scale_width, scale_height))
         images.append(image)



    return images



screen = pygame.display.set_mode((1080, 720))
knight_masks = []
dark_knight = load_sprites(2, 'Dark Knight', 180, 90)
for knight in dark_knight:

    mask = pygame.mask.from_surface(knight)
    knight_masks.append(mask)

bat = load_sprites(4,'bat', 150, 75)
bat_masks = []
for monster in bat:
    mask = pygame.mask.from_surface(monster)
    bat_masks.append(mask)
x_spawn = 0

collected = False
countdown = 0


gkey = pygame.image.load('gkey0.png').convert_alpha()
gkey = pygame.transform.scale(gkey, (75,75))
gkey_rect = make_random_key(gkey.get_width(), gkey.get_height())
gkey_mask = pygame.mask.from_surface(gkey)
gkey_collected = 0

level = 1

knight_rect = dark_knight [0].get_rect()
knight_rect.move_ip(500, 600)

grass = pygame.image.load("grass0.png")

bat_rect = bat [0].get_rect()

clock = pygame.time.Clock()
fps = 60

died = False
win = False

fireball = load_sprites (10, 'fireball0', 32, 32)
fireball_masks = []
for monster in fireball:
    mask = pygame.mask.from_surface(monster)
    fireball_masks.append(mask)


font = pygame.sysfont.SysFont('xxx', 32, True, False)
died_text = font.render('Loss Of Honor', False, (0, 0, 0))
win_text = font.render('Congratulations', False, (255, 255, 255))
start_sound = pygame.mixer.Sound('music.ogg')



ftree = pygame.image.load('Full Tree0.png').convert_alpha()
ftree = pygame.transform.scale(ftree, (600, 400))
tri_mask = pygame.mask.from_surface(ftree)

x = 720

y = 0



tri_rects = []
for count in range(0, 8):
    tree_rect = ftree.get_rect()
    tree_rect.move_ip(-275, count *150)
    tri_rects.append(tree_rect)

for count in range(0, 8):
    tree_rect = ftree.get_rect()
    tree_rect.move_ip(750, count* 150)
    tri_rects.append(tree_rect)

enemies = []



pygame.mouse.set_visible(False)
running = True

count = 0
speed = 10


start_sound.play(20)
while running:


    if win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((0, 0, 0))
        screen.blit(win_text, (400, 300))
        pygame.display.update()
        continue

    if died:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((210, 255, 220))
        screen.blit(grass, [0, 0])
        for tri in tri_rects:
            screen.blit(ftree, tri)
        screen.blit(died_text, [540, 360])
        clock.tick(60)
        pygame.display.update()
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            speed = 20
        if event.type == pygame.MOUSEBUTTONUP:
            speed = 10

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_RIGHT]:
    #     speed = 10
    if keys[pygame.K_w]:
        knight_rect.move_ip(0, -speed)
    if keys[pygame.K_a]:
        knight_rect.move_ip(-speed,0)
    if keys[pygame.K_s]:
        knight_rect.move_ip(0,10)
    if keys[pygame.K_d]:
        knight_rect.move_ip(speed,0)
    if knight_rect.x < 0:
        knight_rect.move_ip(speed,0)
    if knight_rect.x > 1080- dark_knight[0].get_width():
        knight_rect.move_ip(-speed, 0)
    if knight_rect.y > 720 - dark_knight[0].get_height():
        knight_rect.move_ip(0, -speed)

    screen.fill((210, 255, 220))
    screen.blit(grass,[0, 0])


    if count % 100 == 0:
        for num in range (0,8):
            rect = make_random_entity(bat[0].get_width(), bat[0].get_height(), x_spawn)
            enemies.append(rect)

            x_spawn += 1
    x_spawn = 0
    if level == 1:
        bat_frame = int((count / 1) % len(bat))
        enemy_image = bat[bat_frame]
    elif level == 2:
        fireball_frame = int ((count / 1) % len(fireball))
        enemy_image = fireball[fireball_frame]

    sprite_frame = int((count / 5) % len(dark_knight))
    enemies = [b for b in enemies if b.y < 720]

    for b in enemies:
        if level == 1:
            off_x = knight_rect.x - b.x
            off_y = knight_rect.y - b.y

            if bat_masks[bat_frame].overlap(knight_masks[sprite_frame], (off_x, off_y)):
                died = True

            tran_y = 10* math.sin(count% 10 * math.pi /5)
            tran_x = 10* math.cos(count% 10 * math.pi /5)

            b.move_ip (tran_x, 15 + tran_y)
        elif level == 2:
            off_x = knight_rect.x - b.x
            off_y = knight_rect.y - b.y
            if fireball_masks[fireball_frame].overlap(knight_masks[sprite_frame], (off_x, off_y)):
                died = True
            tran_x = 0
            tran_y =  25

            b.move_ip(tran_x, 25 + tran_y)

        else:
            win = True
        screen.blit(enemy_image, b)

    if not collected:

        screen.blit(gkey, gkey_rect)

        off_x = knight_rect.x - gkey_rect.x
        off_y = knight_rect.y - gkey_rect.y

        if gkey_mask.overlap(knight_masks[sprite_frame], (off_x, off_y)):
            gkey_collected += 1
            collected = True
            countdown = 180
    else:
        countdown -= 1
        if countdown == 0:
            collected = False
            gkey_rect = make_random_key(gkey.get_width(), gkey.get_height())
    if gkey_collected == 3:

        level += 1
        enemies = []
        count = 0
        gkey_collected = 0








    m_pos = pygame.mouse.get_pos()


    for tri in tri_rects:
        screen.blit(ftree, tri)




    screen.blit(dark_knight[sprite_frame], knight_rect)

    count += 1
    clock.tick(60)
    pygame.display.update()