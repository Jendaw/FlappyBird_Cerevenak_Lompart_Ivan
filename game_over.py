import os
import pygame
from button import Button

class Menu:
    def __init__(self, screen):
        self.nahraj()
        self.screen  = screen
        self.prev = True
        self.current = False
        self.stngs = Button(self.screen,self.screen.get_width()/2, self.screen.get_height()/2+150, "Settings.png", 150, "black")
        self.startBtn = Button(self.screen, self.screen.get_width()/2, self.screen.get_height()/2+50, "START.png", 100, "black")
        self.titleBtn = Button(self.screen, self.screen.get_width()/2 , 100, "Flappy-Ballz.png", 375, "black", False)

    
    def nahraj(self):
        self.assets_dir = os.path.join(os.path.dirname(__file__), "assets/images")
        self.bg = pygame.image.load(os.path.join(self.assets_dir, "background.png")).convert()
        self.floor = pygame.image.load(os.path.join(self.assets_dir, "floor.png")).convert()
        self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "bird.png")).convert_alpha()

    def zapni(self):
        self.music.menu_music()

    def draw(self):
        for i in range(0,self.screen.get_width(), self.bg.get_width()):
            self.screen.blit(self.bg ,(i,0))

        for i in range(0,self.screen.get_width(),self.floor.get_width()):
            self.screen.blit(self.floor,(i,self.screen.get_height()-self.floor.get_height()))

        self.current = pygame.mouse.get_pressed()[0]

        self.titleBtn.draw()
        self.screen.blit(self.bird_img,(self.screen.get_width()/2-self.bird_img.get_width()/2, self.screen.get_height()/2-self.bird_img.get_height()/2))
        self.startBtn.draw()
        self.stngs.draw()

        if self.stngs.checkHover() and not self.prev and self.current:
            self.prev = self.current
            return "stngs"
        elif self.startBtn.checkHover() and not self.prev and self.current:
            self.prev = self.current
            return "start"
        else:
            self.prev = self.current
            return "menu"