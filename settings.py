import os
import pygame
from button import Button
from pygame_widgets.slider import Slider
import pygame_widgets
class Settings:
    def __init__(self, screen, music, bg, birdImg):
        self.nahraj()
        self.music = music
        self.bird_img = birdImg
        self.bg = bg
        self.screen  = screen
        self.prev = True
        self.current = pygame.mouse.get_pressed()[0]
        self.stngs = Button(self.screen,self.screen.get_width()/2, 40, "Settings.png", 175, "black", False)
        self.fonts_dir = os.path.join(os.path.dirname(__file__), "assets", "fonts")
        font_path = os.path.join(self.fonts_dir, "flappy-font.ttf")
        self.font = pygame.font.Font(font_path, 20)
        self.birdColorText = Button(self.screen, self.screen.get_width()/2, self.screen.get_height()/2-205, "BIRD-COLOR.png",150, "black", False)
        self.birdColorRed = Button(self.screen, self.screen.get_width()/2-75, self.screen.get_height()/2-140, "redbird-upflap.png", 35, "black")
        self.birdColorBlue = Button(self.screen, self.screen.get_width()/2, self.screen.get_height()/2-140, "bird.png", 35, "black")
        self.birdColorYellow = Button(self.screen, self.screen.get_width()/2+75, self.screen.get_height()/2-140, "yellowbird-upflap.png", 35, "black")
        

        self.themeText = Button(self.screen, self.screen.get_width()/2, self.screen.get_height()/2-70, "THEME.png", 130, "black", False)
        self.nightBtn = Button(self.screen, self.screen.get_width()/2-90, self.screen.get_height()/2-10, "NIGHT.png", 90, "black")
        self.dayBtn = Button(self.screen, self.screen.get_width()/2+90, self.screen.get_height()/2-10, "DAY.png", 60, "black")
        
        self.sfxVolume = 50
        self.sfxBtn = Button(self.screen, self.screen.get_width()/2-90, self.screen.get_height()/2+55, "SFX-VOLUME.png", 130, "Black", False)
        self.SfxSlider = Slider(self.screen, int(self.screen.get_width()/2-150), int(self.screen.get_height()/2+100), 125,15, initial=self.sfxVolume)
        
        self.voluem = 50
        self.musicBtn = Button(self.screen, self.screen.get_width()/2+90, self.screen.get_height()/2+55, "MUSIC-VOLUME.png", 160, "Black", False)
        self.voluemSlider = Slider(self.screen, int(self.screen.get_width()/2+25), int(self.screen.get_height()/2+100), 125, 15, initial=self.voluem)
       
        self.BackToMenuBtn = Button(self.screen, self.screen.get_width()/2 , self.screen.get_height()-135, "Back-to-Menu.png", 200, "black")
    
    def nahraj(self):
        self.assets_dir = os.path.join(os.path.dirname(__file__), "assets/images")
        self.bg = pygame.image.load(os.path.join(self.assets_dir, "background.png")).convert()
        self.floor = pygame.image.load(os.path.join(self.assets_dir, "floor.png")).convert()
        self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "bird.png")).convert_alpha()

    def draw(self):
        events = pygame.event.get()
        self.voluem = self.voluemSlider.getValue()
        self.sfxVolume = self.SfxSlider.getValue()
        self.music.setVolume(self.voluem)
        self.music.setSfxVolume(self.sfxVolume)
        for i in range(0,self.screen.get_width(), self.bg.get_width()):
            self.screen.blit(self.bg ,(i,0))

        for i in range(0,self.screen.get_width(),self.floor.get_width()):
            self.screen.blit(self.floor,(i,self.screen.get_height()-self.floor.get_height()))


        self.birdColorText.draw()
        self.birdColorRed.draw()
        self.birdColorYellow.draw()
        self.birdColorBlue.draw()

        self.themeText.draw()
        self.nightBtn.draw()
        self.dayBtn.draw()

        self.BackToMenuBtn.draw()
        self.stngs.draw()
    
        sfxText = self.font.render(str(self.sfxVolume), True, "Black")
        self.screen.blit(sfxText,(self.screen.get_width()/2-97, self.screen.get_height()/2+70))
        self.sfxBtn.draw()
        
        musicText = self.font.render(str(self.voluem), True, "black")
        self.screen.blit(musicText, (self.screen.get_width()/2+77, self.screen.get_height()/2+70))
        
        self.musicBtn.draw()
        
        pygame_widgets.update(events)
        self.current = pygame.mouse.get_pressed()[0]
        if self.nightBtn.checkHover() and not self.prev and self.current:
            self.bg = pygame.image.load(os.path.join(self.assets_dir, "background-night.png")).convert()
        elif self.dayBtn.checkHover() and not self.prev and self.current:
            self.bg = pygame.image.load(os.path.join(self.assets_dir, "background.png")).convert()

        if self.birdColorRed.checkHover() and not self.prev and self.current:
            self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "redbird-upflap.png")).convert_alpha()
        elif self.birdColorYellow.checkHover() and not self.prev and self.current:
            self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "yellowbird-upflap.png")).convert_alpha()
        elif self.birdColorBlue.checkHover() and not self.prev and self.current:
            self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "bird.png")).convert_alpha()
 
        if self.BackToMenuBtn.checkHover() and not self.prev and self.current:
            self.prev = self.current
            return "menu" , self.bg, self.bird_img
        else:
            self.prev = self.current
            return "stngs"

    
