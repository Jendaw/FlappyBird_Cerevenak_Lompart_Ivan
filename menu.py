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
        self.titleBtn = Button(self.screen, self.screen.get_width()/2 , 100, "Flappy-Bird.png", 375, "black", False)
        self.font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "assets/fonts/flappy-font.ttf"), 40)
        self.floor_x = 0

    
    def nahraj(self):
        self.assets_dir = os.path.join(os.path.dirname(__file__), "assets/images")
        self.floor = pygame.image.load(os.path.join(self.assets_dir, "floor.png")).convert()
        self.bird_img = pygame.image.load(os.path.join(self.assets_dir, "bird.png")).convert_alpha()

    def zapni(self):
        self.music.menu_music()

    def draw(self,bg,bird, scores):
        self.bg = bg
        self.scores = scores
        self.high = 0
        if len(self.scores) != 0 :
            self.high = max(self.scores)
 

        self.bird_img = bird
        for i in range(0,self.screen.get_width(), self.bg.get_width()):
            self.screen.blit(self.bg ,(i,0))

        self.floor_x -= 0
        floor_poz = self.floor_x
        while floor_poz < self.screen.get_width():
            self.screen.blit(self.floor, (floor_poz, self.screen.get_height()-self.floor.get_height()))
            floor_poz += self.floor.get_width()
        if self.floor_x <= -self.floor.get_width():
            self.floor_x = 0

        self.current = pygame.mouse.get_pressed()[0]

        score_text = self.font.render("HIGH SCORE: "+str(self.high), True, "red")
        score_rect = score_text.get_rect(center=(self.screen.get_width() / 2, 200))
        self.screen.blit(score_text, score_rect)


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
        
