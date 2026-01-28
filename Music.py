import pygame

class Music():

    def __init__(self):
        pygame.mixer.init()
        self.fail = pygame.mixer.Sound("assets/sounds/fail.wav")
        self.mid = pygame.mixer.Sound("assets/sounds/not_great_not_terrible_loss_party_fukac.wav")
        self.good = pygame.mixer.Sound("assets/sounds/good_win_applause.wav")

    def menu_music(self):
        pygame.mixer.music.load("assets/sounds/menu_music.mp3")
        pygame.mixer.music.play(-1)

    def play_music(self):
        pygame.mixer.music.load("assets/sounds/hracia_muzika.mp3")
        pygame.mixer.music.play(-1)

    def fail_end(self):
        pygame.mixer.music.stop()
        self.fail.play()

    def mid_end(self):
        pygame.mixer.music.stop()
        self.mid.play()


    def good_end(self):
        pygame.mixer.music.stop()
        self.good.play()

    def setVolume(self, volume):
        pygame.mixer.music.set_volume(volume/100)

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