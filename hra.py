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
bird_path = os.path.join(assets_dir, "images", "bird.png")

background = pygame.image.load(bg_path).convert()
background = pygame.transform.scale(background, screen.get_size())

floor_img = pygame.image.load(floor_path).convert_alpha()
floor_height = floor_img.get_height()
floor_img = pygame.transform.scale(floor_img, (screen.get_width(), floor_height))
floor_y = screen.get_height() - floor_img.get_height()

bird_img = pygame.image.load(bird_path).convert_alpha()
bird_w, bird_h = bird_img.get_size()
bird_x = (screen.get_width() - bird_w) / 2
bird_y = (screen.get_height() - bird_h) / 2
bird_vel_y = 0.0
gravity = 0.5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    bird_vel_y += gravity
    bird_y += bird_vel_y
    if bird_y + bird_h >= floor_y:
        bird_y = floor_y - bird_h
        bird_vel_y = 0.0

    screen.blit(background, (0, 0))
    screen.blit(bird_img, (bird_x, bird_y))
    screen.blit(floor_img, (0, floor_y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()