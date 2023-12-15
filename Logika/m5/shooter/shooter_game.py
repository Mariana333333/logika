
#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

lost = 0
score = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.width = player_width
        self.height = player_height
        self.rect =self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width-self.width-10:
            self.rect.x += self.speed

    def fire(self):
        pass

class Enemy(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global lost, score
        if self.rect.y>win_height:
            self.rect.y=0
            self.rect.x=randint(0, win_width-100)
            lost = lost + 1
            score = score + 1

win_width = 700
win_height = 500


window = display.set_mode((win_width, win_height))
background = scale(load('galaxy.jpg'), (win_width, win_height))


ship = Player('rocket.png', 5, win_height-110, 80, 100, 6)


monsters = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png', randint(0, win_width-100), 0, 80, 100, randint(1, 5))
    monsters.add(enemy)

game = True
finish = False

clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
mixer.music.set_volume(0.05)

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        text_lose = font1.render(f'пропущено: {lost}', True, (255, 255, 255))
        text_score = font2.render(f'рахунок: {score}', True, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        ship.reset()
        enemy.reset()
        monsters.draw(window)


        ship.update()
        enemy.update()
        monsters.update()




    display.update()
    clock.tick(FPS)


