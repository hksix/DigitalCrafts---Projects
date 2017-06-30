import pygame, sys, math
from pygame.locals import *
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()



class Hero_sprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 5
    MAX_REVERSE_SPEED = 5
    acceleration = 2
    Turn_speed = 5  #rotaion speed
    
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = self.k_space = 0
    def update(self, deltat):
        #simulation
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < -self.MAX_REVERSE_SPEED:
            self.speed = -self.MAX_REVERSE_SPEED
        self.direction += (self.k_right + self.k_left)
        x, y = self.position
        rad  = self.direction * math.pi/180
        x += -self.speed * math.sin(rad)
        y += -self.speed * math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
    # def drift_m(self):
        if self.k_space:
        # self.drift += self.k_space
            rad = self.direction * (math.pi/80) /(180)
            x += self.speed*(math.sin(rad))
            y += self.speed*(math.cos(rad))
            self.position = (x, y -2)



# class PadSprite(pygame.sprite.Sprite):
#     normal = pygame.image.load('/Users/hamzahaseeb/DigitalCrafts-06-2017/python/pygame-project/images/goblin.png')
#     hit = pygame.image.load('/Users/hamzahaseeb/DigitalCrafts-06-2017/python/pygame-project/images/goblin.png')
#     def __init__(self, number, position):
#         pygame.sprite.Sprite.__init__(self)
#         self.number = number
#         self.rect = pygame.Rect(self.normal.get_rect())
#         self.rect.center = position
#         self.image = self.normal
# pads = [
#     PadSprite(1, (200, 200)),
#     PadSprite(2, (800, 200)),
#     PadSprite(3, (200, 600)),
#     PadSprite(4, (800, 600)),
# ]

rect = screen.get_rect()
hero = Hero_sprite('/Users/hamzahaseeb/DigitalCrafts-06-2017/python/pygame-project/images/hero.png', rect.center)
hero_group = pygame.sprite.RenderPlain(hero)
# pad_group = pygame.sprite.RenderPlain(*pads)
# current_pad_number = 0
# collisions = pygame.sprite.spritecollide(hero_group, pad_group)
# pad_group.update(collisions)
# pad_group.draw(screen)
# pads = pygame.sprite.spritecollide(hero, pads, False)
# if pads:
#     pad = pads[0]
#     if pad.number == current_pad_number + 1:
#         pad.image = pad.hit
#         current_pad_number += 1
#     elif current_pad_number == 4:
#         for pad in pad_group.sprites(): pad.image = pad.normal
#         current_pad_number = 0



while 1:
    deltat = clock.tick(30)
    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue
        down = event.type == KEYDOWN
        if event.key == K_RIGHT:
            hero.k_right = down * -5
           
        if event.key == K_LEFT:
            hero.k_left = down * 5

        if event.key == K_UP:
            hero.k_up = down * -0.5
        if event.key == K_DOWN:
            hero.k_down = down *  -0.5
        if event.key == K_SPACE:
            hero.k_space = down * 0.5
        if event.key == K_ESCAPE:
            sys.exit(0)

    screen.fill((0, 0, 0))
    hero_group.update(deltat)
    hero_group.draw(screen)
    pygame.display.flip()


