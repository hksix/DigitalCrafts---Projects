import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Hero(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 20

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def render(self, screen):
        self.pygame.image.load('/Users/hamzahaseeb/DigitalCrafts-06-2017/python/pygame-project/images/hero.png')
def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Simple Example')

    # Game initialization
    hero = Hero(250, 250)

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.speed_y = 5
                elif event.key == KEY_UP:
                    hero.speed_y = -5
                elif event.key == KEY_LEFT:
                    hero.speed_x = -5
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    hero.speed_y = 0
                elif event.key == KEY_UP:
                    hero.speed_y = 0
                elif event.key == KEY_LEFT:
                    hero.speed_x = 0
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        hero.update()

        # Draw background
        screen.fill(blue_color)

        # Game display
        hero.render(screen)
        font = pygame.font.Font(None, 25)
        text = font.render('Use arrow keys to move the hero smoothly', True, (0, 0, 0))
        screen.blit(text, (80, 230))

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
