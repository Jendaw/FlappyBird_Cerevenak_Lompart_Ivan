import os
import pygame
from button import Button

class Menu:
    def __init__(self, screen):
        self.nahraj()
        self.screen  = screen
        self.startBtn = Button(self.screen, self.screen.get_width()/2, self.screen.get_height()/2+10, "START.png", 200, "black")
        self.titleBtn = Button(self.screen, self.screen.get_width()/2 , self.screen.get_height()/2-100, "Flappy-Ballz.png", 600, "black", False)
    def nahraj(self):
        self.assets_dir = os.path.join(os.path.dirname(__file__), "assets/images")
        self.bg = pygame.image.load(os.path.join(self.assets_dir, "background.png")).convert()
        self.floor = pygame.image.load(os.path.join(self.assets_dir, "floor.png")).convert()
        self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "bird.png")).convert_alpha()

    def draw(self):
        for i in range(0,self.screen.get_width(), self.bg.get_width()):
            self.screen.blit(self.bg ,(i,0))

        for i in range(0,self.screen.get_width(),self.floor.get_width()):
            self.screen.blit(self.floor,(i,self.screen.get_height()-self.floor.get_height()))

        self.titleBtn.draw()
        if self.startBtn.checkHover() and pygame.mouse.get_pressed()[0]:
            self.nigga()
        self.startBtn.draw()

    def nigga(self):
        print("nigga")
    