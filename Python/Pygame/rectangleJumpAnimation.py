import pygame

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

pygame.init()
pygame.display.set_caption("minimal program")
screen = pygame.display.set_mode((540, 360))

rect1 = pygame.Rect(10,10,50,55)

rect1.x += 40
print('x : ', rect1.x)
print('y : ', rect1.y)
print('w : ', rect1.w)
print('h : ', rect1.h)
print('top : ', rect1.top)

speed = [1,7]

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect1.move_ip(speed)

    if rect1.left < 0 or rect1.right > 540:
        speed[0] *= -1
    if rect1.top < 0 or rect1.bottom > 360:
        speed[1] *= -1

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE,rect1)
    pygame.display.update()
