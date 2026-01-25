import sys
import os
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

assets_dir = os.path.join(os.path.dirname(__file__), "assets")
bg_path = os.path.join(assets_dir, "images", "background.png")

background = pygame.image.load(bg_path).convert()
background = pygame.transform.scale(background, screen.get_size())

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()