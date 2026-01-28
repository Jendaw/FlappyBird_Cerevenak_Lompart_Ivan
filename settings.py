import os
import pygame
from button import Button
from pygame_widgets.slider import Slider
import pygame_widgets
class Settings:
    def __init__(self, screen, music):
        self.nahraj()
        self.music = music
        self.screen  = screen
        self.prev = True
        self.current = pygame.mouse.get_pressed()[0]
        self.stngs = Button(self.screen,self.screen.get_width()/2, 75, "Settings.png", 300, "black", False)
        self.voluem = 50
        self.voluemSlider = Slider(self.screen, int(self.screen.get_width()/2-100), int(self.screen.get_height()/2), 200, 20, initial=self.voluem)
        self.BackToMenuBtn = Button(self.screen, self.screen.get_width()/2 , self.screen.get_height()-150, "Back-to-Menu.png", 200, "black")
    
    def nahraj(self):
        self.assets_dir = os.path.join(os.path.dirname(__file__), "assets/images")
        self.bg = pygame.image.load(os.path.join(self.assets_dir, "background.png")).convert()
        self.floor = pygame.image.load(os.path.join(self.assets_dir, "floor.png")).convert()
        self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "bird.png")).convert_alpha()

    def draw(self):
        events = pygame.event.get()
        self.voluem = self.voluemSlider.getValue()
        self.music.setVolume(self.voluem)
        for i in range(0,self.screen.get_width(), self.bg.get_width()):
            self.screen.blit(self.bg ,(i,0))

        for i in range(0,self.screen.get_width(),self.floor.get_width()):
            self.screen.blit(self.floor,(i,self.screen.get_height()-self.floor.get_height()))


        self.BackToMenuBtn.draw()
        self.stngs.draw()
        
        pygame_widgets.update(events)
        self.current = pygame.mouse.get_pressed()[0]
        if self.BackToMenuBtn.checkHover() and not self.prev and self.current:
            self.prev = self.current
            return "menu"
        else:
            self.prev = self.current
            return "stngs"
        
    def nigga(self):
        print("nigga")
    
