import pygame
import sys

if not pygame.font:print('warning fonts disabled')
if not pygame.mixer:print('warning sound disabled')

pygame.init()
clock = pygame.time.Clock()

size = (480, 320)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

CORAL = (255,127,80)
LIGHT_GREEN = (144,238,144)
SKY_BLUE = (135,206,235)

screen = pygame.display.set_mode(size)

height = 50
width = 40
x = 50
y = size[1] - height
speed = 5

running = True

while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    print(keys)
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < size[0] - width:
        x += speed
    if keys[pygame.K_w ] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y < size[1] - height:
        y += speed

    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen,CORAL,(x,y,width,height))
    pygame.display.update()





