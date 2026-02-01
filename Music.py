import pygame
import os

class Music():

    def __init__(self):
        pygame.mixer.init()
        self.sounds_dir = os.path.join(os.path.dirname(__file__), "assets", "sounds")
        self.fail = pygame.mixer.Sound(os.path.join(self.sounds_dir, "fail.wav"))
        self.mid = pygame.mixer.Sound(os.path.join(self.sounds_dir, "not_great_not_terrible_loss_party_fukac.wav"))
        self.good = pygame.mixer.Sound(os.path.join(self.sounds_dir, "good_win_applause.wav"))
        self.bonk = pygame.mixer.Sound(os.path.join(self.sounds_dir, "pipe_bonk.mp3"))

    def menu_music(self):
        self.good.stop()
        pygame.mixer.music.load(os.path.join(self.sounds_dir, "menu_music.mp3"))
        pygame.mixer.music.play(-1)
        self.fail.stop()

    def play_music(self):
        self.good.stop()
        pygame.mixer.music.load(os.path.join(self.sounds_dir, "hracia_muzika.mp3"))
        pygame.mixer.music.play(-1)
        self.fail.stop()

    def fail_end(self):
        pygame.mixer.music.stop()
        self.fail.play()

    def mid_end(self):
        pygame.mixer.music.stop()
        self.mid.play()

    def good_end(self):
        pygame.mixer.music.stop()
        self.good.play()

    def pipe_bonk(self):
        self.bonk.play()

    def jump(self):
        self.bonk.play()

    def setVolume(self, volume):
        pygame.mixer.music.set_volume(volume/100)
    
    def setSfxVolume(self,volume):
        self.fail.set_volume(volume/100)
        self.mid.set_volume(volume/100)
        self.good.set_volume(volume/100)
        self.bonk.set_volume(volume/100)

    def getVolume(self):
        return pygame.mixer.music.get_volume()

"""
k = Music()
k.menu_music()
input()
k.fail_end()
input()
k.menu_music()
input()
k.play_music()
input()
k.mid_end()
input()
k.good_end()
input()
"""