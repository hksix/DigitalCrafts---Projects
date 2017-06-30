import pygame
import math

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    
 
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    monster_x = 0
    monster_y = 0
    hero = pygame.image.load('/Users/hamzahaseeb/DigitalCrafts-06-2017/python/pygame-project/images/hero.png')
    # background_image = pygame.image.load('/Users/hamzahaseeb/DigitalCrafts-06-2017/python/pygame-project/images/background.png').convert_alpha()
    rotated = pygame.transform.rotate(hero, 45 * math.pi / 180)

#comment

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(hero, (50, 100))
        # screen.blit(background_image, (0, 0))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
