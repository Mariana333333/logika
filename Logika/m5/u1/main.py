import time

from pygame import *

window = display.set_mode((700, 500))


img = image.load("background.png")
background = transform.scale(img, (700, 500))

clock = time.Clock()
FPS = 60
SPEED = 10

sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))
x1 = 200
y1 = 300


sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))
x2 = 400
y2 = 200

window.blit(background, (0, 0))

game = True

while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))


    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= SPEED

    if keys_pressed[K_RIGHT] and x1 < 610:
        x1 += SPEED

    if keys_pressed[K_UP] and y1 > 5:
        y1 -= SPEED

    if keys_pressed[K_DOWN] and y1 < 400:
        y1 += SPEED

    display.update()
    clock.tick(FPS)