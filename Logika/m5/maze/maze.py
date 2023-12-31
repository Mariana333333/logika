import time

from pygame import*
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect =self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width-80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= win_width-80:
            self.direction = 'left'

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((0, 225, 0))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



win_width = 700
win_height= 500

window = display.set_mode((win_width, win_height))

background = scale(load("background.jpg"), (win_width, win_height))

player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 150, win_height - 300, 2)
final = GameSprite('treasure.png', win_width-80, win_height-80, 0)
wall1 = Wall(0, 320, 100, 10)


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()

font = font.Font(None, 70)

win = font.render('VICTORY!!!', True, (60, 67, 200))
lose = font.render('GAME OVER!!!', True, (250, 0, 10))


mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play(-1)


money_sound = mixer.Sound('money.ogg')
kick_sound = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player.reset()
        monster.reset()
        final.reset()
        wall1.reset()

        player.update()
        monster.update()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money_sound.play()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall1):
            finish = True
            window.blit(lose, (200, 200))
            kick_sound.play()



    display.update()
    clock.tick(FPS)





