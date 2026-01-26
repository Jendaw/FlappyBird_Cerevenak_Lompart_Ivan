import sys
import os
import pygame

class Button:
    def __init__(self, screen, x, y, text):
        self.screen = screen
        self.x = x
        self.y = y
        self.text = text
    
    def draw(self):
        font = pygame.Font("assets/fonts/flappy-font.ttf", size=20)

class Bird:
    def __init__(self, screen, x, y, bird_img):
        self.screen = screen
        self.bird_img = bird_img
        self.bird_rect = self.bird_img.get_rect()
        self.bird_rect.centerx = x
        self.bird_rect.centery = y
        self.bird_rect.width, self.bird_rect.height = self.bird_img.get_size()
        self.bird_vel_y = 0
        self.gravity = 0.5

    def jump(self):
        self.bird_vel_y = -8

    def draw(self):
        self.screen.blit(self.bird_img, (self.bird_rect.x, self.bird_rect.y))

    def update(self):
        self.bird_vel_y += self.gravity
        self.bird_rect.y += self.bird_vel_y
        if 0 > self.bird_rect.top:
            self.bird_vel_y = 0
            self.bird_rect.top =0

class Hra:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.nahraj()

    def draw(self):
        self.floor_rect = self.floor.get_rect()
        self.floors = []

        i = 0
        while i < self.screen.get_width():
             self.screen.blit(self.bg, (i , 0))
             i+=self.bg.get_width()

        j = 0
        while j < self.screen.get_width():
            self.floor_rect.x = j
            self.floor_rect.y = self.screen.get_height()-self.floor.get_height()
            self.screen.blit(self.floor, (self.floor_rect.x, self.floor_rect.y))
            self.floors.append(self.floor_rect.copy())
            j+=self.floor.get_width()


    def nahraj(self):
        self.assets_dir = os.path.join(os.path.dirname(__file__), "assets/images")
        self.bg = pygame.image.load(os.path.join(self.assets_dir, "background.png")).convert()
        self.floor = pygame.image.load(os.path.join(self.assets_dir, "floor.png")).convert()
        self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "bird.png")).convert_alpha()

    def collision(self):
        if self.bird.bird_rect.collidelist(self.floors) != -1:
            self.bird.bird_vel_y = 0
            self.bird.bird_rect.bottom = self.screen.get_height()-self.floor.get_height()

    def run(self):
        self.bird = Bird(self.screen, self.screen.get_width()/2,self.screen.get_height()/2, self.bird_img)
        pygame.font.init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bird.jump()

            self.draw()
            self.bird.update()
            self.collision()
            self.bird.draw()
            pygame.display.flip()
            self.clock.tick(60)


hra = Hra()
hra.run()