
import pygame
import random

def make_square(x,y):

    square = pygame.rect.Rect(x,y, 10, 10)

    return square

def make_random_entity(width, height):
    x = random.randint(0, 719)
    y = random.randint(0, 719)
    rect = pygame.rect.Rect(x, y, width, height)
    return rect

pygame.init()
pygame.key.set_repeat(10,10)

screen = pygame.display. set_mode((1080,720))

clock = pygame.time.Clock()
fps = 120


font = pygame.sysfont.SysFont('xxx', 32, True, False)
died_text = font.render('Loss Of Honor', False, (0, 0, 0))


start_sound = pygame.mixer.Sound('music.ogg')


x = 720

y = 0

square = make_square(50, 100)

images = []
masks = []
path = 'Dark Knight'

for count in range (1,3):

    image = pygame.image.load(path + str(count) + ".png").convert_alpha()
    image = pygame.transform.scale(image, (80,120))
    images.append(image)



    mask = pygame.mask.from_surface(image)
    masks.append(mask)
image_rect = images[0].get_rect()

#     pygame.image.load('Dark Knight0.png').convert_alpha()
# image2 = pygame.image.load('Dark Knight1.png').convert_alpha()



tree = pygame.image.load('Full Tree0.png').convert_alpha()
tree = pygame.transform.scale(tree, (600, 400))
tri_mask = pygame.mask.from_surface(tree)

tri_rects = []

for count in range (0, 10):
    rand_tri = make_random_entity(tree.get_width(), tree.get_height())

    tri_rects.append(rand_tri)











pygame.mouse.set_visible(False)
running = True

count = 0
# Game loop

start_sound.play()
while running:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        image_rect.move_ip(0, -3)
    if keys[pygame.K_a]:
        image_rect.move_ip(-3,0)
    if keys[pygame.K_s]:
        image_rect.move_ip(0,3)
    if keys[pygame.K_d]:
        image_rect.move_ip(3,0)


    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #
        #     if event.key == pygame.K_w:
        #         image_rect.move_ip(0, -5)
        #     if event.key == pygame.K_a:
        #         image_rect.move_ip(-5,0)
        #
        #     if event.key == pygame.K_s:
        #         image_rect.move_ip(0,5)
        #
        #     if event.key == pygame.K_d:
        #         image_rect.move_ip(5,0)

    screen.fill((210,255,220))
    speed = 200
    m_pos = pygame.mouse.get_pos()


    #
    # image_rect.x = m_pos[0] - 300
    # image_rect.y = m_pos[1] - 150

    # if count % speed < speed/2:
    #     screen.blit(images[0], image_rect)
    # else:
    #     screen.blit(images[1], image_rect)
    sprite_frame = int((count/55) % len(images))






    for tri in tri_rects:
        screen.blit(tree, tri)

        off_x = image_rect.x - tri.x
        off_y = image_rect.y - tri.y

        if tri_mask.overlap(masks[sprite_frame], (off_x, off_y)):
            screen.blit(died_text, [350, 350])
    screen.blit(images[sprite_frame], image_rect)

    # screen.blit(tree, (300, 300))

    # pygame.draw.rect(screen, (255, 255, 255), square)





    # if square.colliderect(image_rect):
    #     screen.blit(died_text, [350, 350])

        #pygame.display.update()
        # clock.wait(1000)

    count += 1
    pygame.display.update()