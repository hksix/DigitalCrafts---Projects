import pygame, sys, math
from pygame.locals import *
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
pygame.init()

class Hero_sprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 15
    MAX_REVERSE_SPEED = 15
    acceleration = 2
    Turn_speed = 5  #rotaion speed
    
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speed = self.direction = -8
        self.k_left = self.k_right = self.k_down = self.k_up = self.k_space = 0
        self.radius = 50
        self.health = 10
        
    def update(self, deltat):
        #simulation
        self.health_counter()
        self.wall_bounce()
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
        # print self.position
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        if self.k_space:
                # self.speed = -5
                rad = self.direction * (math.pi/80) /(180)
                x -= self.speed*(math.sin(rad))
                y += self.speed*(math.cos(rad)) 
                self.position = (x, y)
        
        
    def wall_bounce(self):
        x, y = self.position
        if x > 1000:    
            if self.speed > 0:
                self.speed = -100
            else:
                self.speed = + 100
            self.health -= 1
        if x < 20:
            if self.speed > 0:
                self.speed = -100
            else:
                self.speed = + 100
            self.health -= 1   
        if y < 20:
            if self.speed > 0:
                self.speed = -100
            else:
                self.speed = + 100
            self.health -= 1
        if y > 768:
            if self.speed > 0:
                self.speed = -100
            else:
                self.speed = + 100
            self.health -= 10
        if self.health == 0:
            self.dead()

    def dead(self):
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('GAME    OVER', True, (255, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery
        screen.blit(text, textrect)
        self.position = textrect.centerx, textrect.centery
    
    def health_counter(self):
        x, y = self.position
        basicfont = pygame.font.SysFont(None, 14)
        text = basicfont.render("health", True, (255, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = x #screen.get_rect().centerx
        textrect.centery = y+30 #screen.get_rect().centery
        screen.blit(text, textrect)
        # self.position = textrect.centerx, textrect.centery
   


rect = screen.get_rect()
hero = Hero_sprite('/Users/hamzahaseeb/DigitalCrafts-06-2017/python/pygame-project/images/hero.png', rect.center)
hero_group = pygame.sprite.RenderPlain(hero)
hero.health_counter()

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
            hero.k_up = down * 0.5
        if event.key == K_DOWN:
            hero.k_down = down *  -0.5
        if event.key == K_SPACE:
            hero.k_space = down * 1.8
            
        if event.key == K_ESCAPE:
            sys.exit(0)

    screen.fill((0, 0, 0))
    hero_group.update(deltat)
    hero_group.draw(screen)
    pygame.display.flip()


