import sys
import os
import pygame
import random
from menu import Menu
from settings import Settings
from Music import Music
from game_over import Menu as GameOver

class Bird:
    def __init__(self, screen, x, y, birdImg):
        self.screen = screen
        self.bird_img = birdImg
        self.bird_rect = self.bird_img.get_rect()
        self.bird_rect.centerx = x
        self.bird_rect.centery = y
        self.bird_rect.width, self.bird_rect.height = self.bird_img.get_size()
        self.bird_vel_y = 0
        self.gravity = 0.5

    def jump(self):
        self.bird_vel_y = -8

    def draw(self,birdImg):
        self.screen.blit(birdImg, (self.bird_rect.x, self.bird_rect.y))

    def update(self, floor_y):
        self.bird_vel_y += self.gravity
        self.bird_rect.y += self.bird_vel_y
        if 0 > self.bird_rect.top:
            self.bird_vel_y = 0
            self.bird_rect.top = 0
        if self.bird_rect.bottom > floor_y:
            self.bird_rect.bottom = floor_y
            self.bird_vel_y = 0

class Hra:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.nahraj()
        pygame.display.set_icon(self.bird_img)

        self.pipe_speed = 3
        self.pipe_min_h = 120
        self.pipe_max_h = 350
        self.gap = 150
        self.pipe_img_top = pygame.transform.flip(self.pipe_img, False, True)
        self.pipe_count = 3
        self.pipe_spacing = 200
        self.pipe_scale_x = 1.0
        self.pipes = []
        self.currentScreen = "menu"
        self.music = Music()
        self.music_playing = None
        self.need_reset = True
        self.score = 0
        self.font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "assets/fonts/flappy-font.ttf"), 40)


        self.settings = Settings(self.screen, self.music, self.bg, self.bird_img)
        self.menu = Menu(self.screen)
        self.gameover = GameOver(self.screen)

    def reset_gameplay(self):
        self.bird = Bird(self.screen, self.screen.get_width()/2, self.screen.get_height()/2, self.bird_img)
        self.floor_y = self.screen.get_height()-self.floor.get_height()
        self.pipes = []
        start_x = self.screen.get_width()+100
        for i in range(self.pipe_count):
            self.pipes.append(self.dvojica(start_x+i*self.pipe_spacing, self.floor_y))
        self.score = 0

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
        self.bg_night = pygame.image.load(os.path.join(self.assets_dir, "background-night.png")).convert()
        self.floor = pygame.image.load(os.path.join(self.assets_dir, "floor.png")).convert()
        self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "bird.png")).convert_alpha()
        self.pipe_img = pygame.image.load(os.path.join(self.assets_dir, "pipe.png")).convert_alpha()

    def dvojica(self, x, floor_y):
        while True:
            bottom_h = random.randint(self.pipe_min_h, self.pipe_max_h)
            top_h = floor_y-bottom_h-self.gap
            if top_h >= 80:
                break

        pipe_w = max(1, int(self.pipe_img.get_width()*self.pipe_scale_x))

        bottom1 = pygame.transform.scale(self.pipe_img, (pipe_w, bottom_h))
        bottom_rect = bottom1.get_rect()
        bottom_rect.bottom = floor_y
        bottom_rect.left = x

        top1 = pygame.transform.scale(self.pipe_img_top, (pipe_w, top_h))
        top_rect = top1.get_rect()
        top_rect.left = x
        top_rect.bottom = bottom_rect.top-self.gap

        return {"bottom1": bottom1, "bottom_rect": bottom_rect,"top1": top1,"top_rect": top_rect, "passed": False}

    def collision(self):
        if self.currentScreen != "start":
            return
        for pipe in self.pipes:
            if self.bird.bird_rect.colliderect(pipe["bottom_rect"]) or self.bird.bird_rect.colliderect(pipe["top_rect"]):
                self.music.fail_end()
                self.currentScreen = "gameover"
                self.need_reset = True
                return

    def run(self):
        pygame.font.init()
        self.reset_gameplay()
        self.need_reset = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.currentScreen == "start":
                    self.bird.jump()
            # print(pygame.mouse.get_pressed()[0])
            if self.currentScreen == "menu":
                if self.music_playing != "menu":
                    self.music.menu_music()
                    self.music_playing = "menu"
                self.currentScreen = self.menu.draw(self.bg, self.bird_img)
            elif self.currentScreen == "stngs":
                self.ret = list(self.settings.draw())
                if type(self.ret[1]) == type(self.bg):
                    self.currentScreen = self.ret[0]
                    self.bg = self.ret[1]
                    self.bird_img = self.ret[2]
            elif self.currentScreen == "start":
                if self.need_reset:
                    self.reset_gameplay()
                    self.need_reset = False
                if self.music_playing != "start":
                    self.music.play_music()
                    self.music_playing = "start"
                self.screen.fill("black")
                self.draw()

                max_left = max(pipe["bottom_rect"].left for pipe in self.pipes)
                for idx, pipe in enumerate(self.pipes):
                    pipe["bottom_rect"].x -= self.pipe_speed
                    pipe["top_rect"].x -= self.pipe_speed

                    if not pipe["passed"] and pipe["bottom_rect"].centerx < self.bird.bird_rect.centerx:
                        pipe["passed"] = True
                        self.score += 1

                    if pipe["bottom_rect"].right < 0:
                        max_left = max(p["bottom_rect"].left for p in self.pipes)
                        self.pipes[idx] = self.dvojica(max_left+self.pipe_spacing, self.floor_y)

                for pipe in self.pipes:
                    self.screen.blit(pipe["top1"], pipe["top_rect"])
                    self.screen.blit(pipe["bottom1"], pipe["bottom_rect"])

                score_text = self.font.render(str(self.score), True, (255, 255, 255))
                score_rect = score_text.get_rect(center=(self.screen.get_width() / 2, 50))
                self.screen.blit(score_text, score_rect)

                self.bird.update(self.floor_y)
                self.collision()
                self.bird.draw(self.bird_img)

            elif self.currentScreen == "gameover":
                if self.music_playing != "gameover":
                    self.music_playing = "gameover"
                nxt = self.gameover.draw(self.score)
                if nxt == "start":
                    self.currentScreen = "start"
                elif nxt == "menu":
                    self.currentScreen = "menu"
                else:
                    self.currentScreen = "gameover"

            pygame.display.flip()
            self.clock.tick(60)

hra = Hra()
hra.run()