import pygame, sys, math
from pygame.locals import *

    
# def main():
class fwd_bck(object):
    def __init__(self, speed_y):
        # self.y = y
        self.speed_y = 0
   

k_up = fwd_bck(5)
k_down = fwd_bck(5)



screen = pygame.display.set_mode((1024, 768))
hero = pygame.image.load('/Users/hamzahaseeb/DigitalCrafts-06-2017/python/pygame-project/images/hero.png')
clock = pygame.time.Clock()
k_left = k_right = k_space = 0
speedup = 0
speeddown = 0
speed = 0
direction = 0
drift = 0
position = (400, 500)
rotation_speed = 0
acceleration = 2
MAX_FORWARD_SPEED = 5
MAX_REVERSE_SPEED = -5
black = (0,0,0)
while 1:

    clock.tick(30)
    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue
        down = event.type == KEYDOWN
        # up = event.type == KEYUP
        if event.key == K_RIGHT:
            k_right = down * -5
           
        if event.key == K_LEFT:
            k_left = down * 5
            
        if event.key == K_UP:
            k_up.speed_y = -1
        if event.key == K_DOWN:
            k_down.speed_y =  -1
            
        if event.key == K_SPACE:
            k_space = down * 0.5
        if event.key == K_ESCAPE:
            sys.exit(0)
        screen.fill(black)


    speeddown -= (k_up.speed_y)
    speed += (k_down.speed_y)

    if speeddown > MAX_FORWARD_SPEED:
        speed = MAX_FORWARD_SPEED
    if speed < MAX_REVERSE_SPEED:
        speedown = MAX_REVERSE_SPEED
    
    direction += (k_right + k_left)


        


    
    r_x, r_y = position
    rad  = direction * math.pi/180
    r_x += -speed * math.sin(rad)
    r_y += -speed * math.cos(rad)
    position = (r_x, r_y)

        

    if k_space:
        # drift -= (k_space)
        turn = direction * (math.pi/80) / 180
        r_x += speed*math.sin(turn)
        r_y -= speed*math.cos(turn)
        position = (r_x, r_y)
        
    rotated = pygame.transform.rotate(hero, direction)

    rect = rotated.get_rect()
    rect.center = position

    screen.blit(rotated, rect)
    
    pygame.display.flip()

