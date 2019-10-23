import sys, pygame, random
def randomMove(oldLocation):
    direction = random.randint(0,3)
    newLocation = oldLocation
    direction = random.randint (0,3)
    newLocation= location

    if direction == 0:
        newLocation[0] -= 1
    if direction == 1:
        newLocation[1] += 1
    if direction == 2:
        newLocation[0] += 1
    if direction == 3:
        newLocation[1] -= 1
    return newLocation

pygame.init()

size = width, height = 500,000
screen = pygame.display.set_mode(size)
screen.fill([0,0,0])

white = [177,43,142]
location = [250,250]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    location = randomMove (location)
    screen.set_at(location,white)
    pygame.display.flip()
