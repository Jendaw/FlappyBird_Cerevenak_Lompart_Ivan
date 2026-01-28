import pygame

class Music():

    def __init__(self):
        pygame.mixer.init()
        self.fail = pygame.mixer.Sound("fail.wav")
        self.mid = pygame.mixer.Sound("not_great_not_terrible_loss_party_fukac.wav")
        self.good = pygame.mixer.Sound("good_win_applause.wav")

    def menu_music(self):
        pygame.mixer.music.load("menu_music.mp3")
        pygame.mixer.music.play(-1)

    def play_music(self):
        pygame.mixer.music.load("hracia_muzika.mp3")
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
input()"""