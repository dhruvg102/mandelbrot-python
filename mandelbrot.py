import pygame, sys, random


def pixel(surface, color, pos):
    pygame.draw.line(surface, color, pos, pos)

def remap(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2




screenH = 520
screenW = 520
x = 0
y = 0
bright = 200
max_iterations = 100


pygame.init()


screen = pygame.display.set_mode((screenW, screenH))
screen.fill((45,45,45))

while x < screenW:
    while y < screenH:
        a = remap(x, 0 ,screenW, -2, +2)
        b = remap(y, 0 ,screenH, -2, +2)

        ca = a
        cb = b

        n = 0
        z = 0

        while n < max_iterations:
            aa = a * a - b * b
            bb = 2 * a * b

            a = aa + ca
            b = bb + cb

            if abs(aa + bb) > 16:
                break

            n += 1

        bright = remap(n, 0, max_iterations, 0, 255)
        if n == max_iterations:
            bright = 0

        pixel(screen, [bright, bright, bright], [x, y])

        y += 1
    x += 1
    y=0


while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.update();
