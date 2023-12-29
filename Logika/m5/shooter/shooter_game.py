
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
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global lost, score
        if self.rect.y>win_height:
            self.rect.y=0
            self.rect.x=randint(0, win_width-100)
            lost = lost + 1



class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y < 0:
            self.kill()

win_width = 700
win_height = 500


window = display.set_mode((win_width, win_height))
background = scale(load('galaxy.jpg'), (win_width, win_height))


ship = Player('rocket.png', 5, win_height-110, 80, 100, 6)


bullets = sprite.Group()
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png', randint(0, win_width-100), 0, 80, 100, randint(1, 3))
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
font3 = font.SysFont('Arial', 80)
txt_lose_game = font3.render('YOU LOSE!', True, (255, 0, 0))
txt_win_game = font3.render('YOU WIN!', True, (0, 255, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                ship.fire()

    if not finish:
        window.blit(background, (0, 0))
        text_lose = font1.render(f'пропущено: {lost}', True, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        text_score = font1.render(f'рахунок: {score}', True, (255, 255, 255))
        window.blit(text_score, (10, 10))
        ship.reset()
        enemy.reset()
        bullets.draw(window)
        monsters.draw(window)




        ship.update()
        enemy.update()
        monsters.update()
        bullets.update()

        if sprite.spritecollide(ship, monsters, False):
            finish = True
            window.blit(txt_lose_game, (200, 200))
        collide = sprite.groupcollide(monsters, bullets, True, True)
        for c in collide:
            enemy = Enemy('ufo.png', randint(0, win_width - 100), 0, 80, 100, randint(1, 5))
            monsters.add(enemy)
            score = score + 1

        if score == 10:
            finish = True
            window.blit(txt_win_game, (200, 200))
    else:
        score = 0
        lost = 0
        finish = False

        for m in monsters:
            m.kill()

        for m in bullets:
            m.kill()



        time.delay(3000)
        for i in range(5):
            enemy = Enemy('ufo.png', randint(0, win_width - 100), 0, 80, 100, randint(1, 3))
            monsters.add(enemy)





    display.update()
    clock.tick(FPS)


