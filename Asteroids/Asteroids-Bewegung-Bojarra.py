from ast import Set
from re import S
import pygame
from pygame.version import PygameVersion
import os

class Settings():
    window = {'width':1000, 'height':1000, 'border':10}
    path_file = os.path.dirname(os.path.abspath(__file__))
    path_image = os.path.join(path_file, "images")
    fps = 60
    caption = "Asteriods"
    rotation = 0

    @staticmethod
    def dim():
        return (Settings.window['width'], Settings.window['height'])

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, filename1, filename2, filename3, filename4, filename5, filename6, filename7, filename8, filename9, filename10, filename11, filename12, filename13, filename14, filename15, filename16) -> None:
        super().__init__()
        self.image_1 = pygame.image.load(os.path.join(Settings.path_image, filename1)).convert()
        self.image_2 = pygame.image.load(os.path.join(Settings.path_image, filename2)).convert()
        self.image_3 = pygame.image.load(os.path.join(Settings.path_image, filename3)).convert()
        self.image_4 = pygame.image.load(os.path.join(Settings.path_image, filename4)).convert()
        self.image_5 = pygame.image.load(os.path.join(Settings.path_image, filename5)).convert()
        self.image_6 = pygame.image.load(os.path.join(Settings.path_image, filename6)).convert()
        self.image_7 = pygame.image.load(os.path.join(Settings.path_image, filename7)).convert()
        self.image_8 = pygame.image.load(os.path.join(Settings.path_image, filename8)).convert()
        self.image_9 = pygame.image.load(os.path.join(Settings.path_image, filename9)).convert()
        self.image_10 = pygame.image.load(os.path.join(Settings.path_image, filename10)).convert()
        self.image_11 = pygame.image.load(os.path.join(Settings.path_image, filename11)).convert()
        self.image_12 = pygame.image.load(os.path.join(Settings.path_image, filename12)).convert()
        self.image_13 = pygame.image.load(os.path.join(Settings.path_image, filename13)).convert()
        self.image_14 = pygame.image.load(os.path.join(Settings.path_image, filename14)).convert()
        self.image_15 = pygame.image.load(os.path.join(Settings.path_image, filename15)).convert()
        self.image_16 = pygame.image.load(os.path.join(Settings.path_image, filename16)).convert()
        self.image = self.image_1
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (Settings.window['width'] // 2, Settings.window['height'] // 2)
        self.directionx = 0
        self.directiony = 0
        self.speed = 2

    def update(self):
        newrect = self.rect.move(self.directionx * self.speed, self.directiony * self.speed)
        if newrect.right >= Settings.window['width']:
            self.rect.centerx -= Settings.window['width']
        if newrect.left <= Settings.window['border']:
            self.rect.centerx += Settings.window['width']
        if newrect.bottom >= Settings.window['height']:
            self.rect.centery -= Settings.window['height']
        if newrect.top <= Settings.window['border']:
            self.rect.centery += Settings.window['height']
        self.rect.move_ip((self.directionx * self.speed, self.directiony * self.speed))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):                     #Entschuldigung
        if Settings.rotation == 0:
            self.directiony -= 3
        if Settings.rotation == 1:
            self.directiony -= 2
            self.directionx -= 1
        if Settings.rotation == 2:
            self.directiony -= 2
            self.directionx -= 2
        if Settings.rotation == 3:
            self.directiony -= 1
            self.directionx -= 2
        if Settings.rotation == 4:
            self.directionx -= 3
        if Settings.rotation == 5:
            self.directiony += 1
            self.directionx -= 2
        if Settings.rotation == 6:
            self.directiony += 2
            self.directionx -= 2
        if Settings.rotation == 7:
            self.directiony += 2
            self.directionx -= 1
        if Settings.rotation == 8:
            self.directiony += 3
        if Settings.rotation == 9:
            self.directiony += 2
            self.directionx += 1
        if Settings.rotation == 10:
            self.directiony += 2
            self.directionx += 2
        if Settings.rotation == 11:
            self.directiony += 1
            self.directionx += 2
        if Settings.rotation == 12:
            self.directionx += 3
        if Settings.rotation == 13:
            self.directiony -= 1
            self.directionx += 2
        if Settings.rotation == 14:
            self.directiony -= 2
            self.directionx += 2
        if Settings.rotation == 15:
            self.directiony -= 2
            self.directionx += 1

    def turnleft(self):
        if Settings.rotation <= 14:
            Settings.rotation += 1
        else:
            Settings.rotation = 0

    def turnright(self):
        if Settings.rotation >= 1:
            Settings.rotation -= 1
        else:
            Settings.rotation = 15

class Game(object):
    def __init__(self) -> None:
        super().__init__()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "50,30"
        pygame.init()
        pygame.display.set_caption(Settings.caption)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.screen = pygame.display.set_mode(Settings.dim())
        self.clock = pygame.time.Clock()
        self.running = False
        self.spaceship = Spaceship("0°Ohne Schiff.bmp",
            "22,5°Ohne Schiff.bmp",
            "45°Ohne Schiff.bmp",
            "67,5°Ohne Schiff.bmp",
            "90°Ohne Schiff.bmp",
            "112,5°Ohne Schiff.bmp",
            "135°Ohne Schiff.bmp",
            "157,5°Ohne Schiff.bmp",
            "180°Ohne Schiff.bmp",
            "202,5°Ohne Schiff.bmp",
            "225°Ohne Schiff.bmp",
            "247,5°Ohne Schiff.bmp",
            "270°Ohne Schiff.bmp",
            "292,5°Ohne Schiff.bmp",
            "315°Ohne Schiff.bmp",
            "337,5°Ohne Schiff.bmp")

    def run(self):
        self.running = True 
        while self.running:
            self.clock.tick(Settings.fps)
            self.watch_for_events()
            self.update()
            self.draw()

        pygame.quit()

    def check_for_rotation(self):
        if Settings.rotation == 0:
            self.spaceship.image = self.spaceship.image_1
        if Settings.rotation == 1:
            self.spaceship.image = self.spaceship.image_2
        if Settings.rotation == 2:
            self.spaceship.image = self.spaceship.image_3
        if Settings.rotation == 3:
            self.spaceship.image = self.spaceship.image_4
        if Settings.rotation == 4:
            self.spaceship.image = self.spaceship.image_5
        if Settings.rotation == 5:
            self.spaceship.image = self.spaceship.image_6
        if Settings.rotation == 6:
            self.spaceship.image = self.spaceship.image_7
        if Settings.rotation == 7:
            self.spaceship.image = self.spaceship.image_8
        if Settings.rotation == 8:
            self.spaceship.image = self.spaceship.image_9
        if Settings.rotation == 9:
            self.spaceship.image = self.spaceship.image_10
        if Settings.rotation == 10:
            self.spaceship.image = self.spaceship.image_11
        if Settings.rotation == 11:
            self.spaceship.image = self.spaceship.image_12
        if Settings.rotation == 12:
            self.spaceship.image = self.spaceship.image_13
        if Settings.rotation == 13:
            self.spaceship.image = self.spaceship.image_14
        if Settings.rotation == 14:
            self.spaceship.image = self.spaceship.image_15
        if Settings.rotation == 15:
            self.spaceship.image = self.spaceship.image_16

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.spaceship.draw(self.screen)

        pygame.display.flip()

    def update(self):
        self.check_for_rotation()
        self.spaceship.update()

    def watch_for_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_UP:
                        self.spaceship.move()
                    elif event.key == pygame.K_LEFT:
                        self.spaceship.turnleft()
                    elif event.key == pygame.K_RIGHT:
                        self.spaceship.turnright()

if __name__ == "__main__":

    game = Game()
    game.run()