import os
import pygame
from button import Button

class Menu:
    def __init__(self, screen):
        self.nahraj()
        self.screen  = screen
        self.prev = True
        self.current = False
        self.menuBtn = Button(self.screen,self.screen.get_width()/2 - 80, self.screen.get_height()/2+150, "Back-to-Menu.png", 150, "black")
        self.startBtn = Button(self.screen, self.screen.get_width()/2 + 80, self.screen.get_height()/2+150, "START.png", 100, "black")
        self.titleBtn = Button(self.screen, self.screen.get_width()/2 , 150, "GAME-OVER.png", 375, "black", False)
        self.font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "assets/fonts/flappy-font.ttf"), 40)


    def nahraj(self):
        self.assets_dir = os.path.join(os.path.dirname(__file__), "assets/images")
        self.floor = pygame.image.load(os.path.join(self.assets_dir, "floor.png")).convert()

    def zapni(self):
        self.music.menu_music()

    def draw(self, score, bg, scores, newHigh):
        self.scores = scores
        self.newHigh = newHigh
        self.high_score = max(self.scores)
        self.bg = bg
        for i in range(0,self.screen.get_width(), self.bg.get_width()):
            self.screen.blit(self.bg ,(i,0))

        for i in range(0,self.screen.get_width(),self.floor.get_width()):
            self.screen.blit(self.floor,(i,self.screen.get_height()-self.floor.get_height()))

        self.current = pygame.mouse.get_pressed()[0]

        self.titleBtn.draw()
        newHigh_text = self.font.render("NEW HIGH SCORE", True, "red")
        newHigh_rect = newHigh_text.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        if self.newHigh:
            self.screen.blit(newHigh_text, newHigh_rect)

        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2-50))
        self.screen.blit(score_text, score_rect)

        self.startBtn.draw()
        self.menuBtn.draw()

        if self.menuBtn.checkHover() and not self.prev and self.current:
            self.prev = self.current
            return "menu"
        elif self.startBtn.checkHover() and not self.prev and self.current:
            self.prev = self.current
            return "start"
        else:
            self.prev = self.current
            return "gameover"