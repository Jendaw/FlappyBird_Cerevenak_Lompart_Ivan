import sys
import os
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

assets_dir = os.path.join(os.path.dirname(__file__), "assets")
bg_path = os.path.join(assets_dir, "images", "background.png")
floor_path = os.path.join(assets_dir, "images", "floor.png")

background = pygame.image.load(bg_path).convert()
background = pygame.transform.scale(background, screen.get_size())

floor_img = pygame.image.load(floor_path).convert_alpha()
floor_height = floor_img.get_height()
floor_img = pygame.transform.scale(floor_img, (screen.get_width(), floor_height))
floor_y = screen.get_height() - floor_img.get_height()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(floor_img, (0, floor_y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()