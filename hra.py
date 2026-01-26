import sys
import os
import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

assets_dir = os.path.join(os.path.dirname(__file__), "assets")
bg_path = os.path.join(assets_dir, "images", "background.png")
floor_path = os.path.join(assets_dir, "images", "floor.png")
bird_path = os.path.join(assets_dir, "images", "bird.png")
pipe_path = os.path.join(assets_dir, "images", "pipe.png")

background = pygame.image.load(bg_path).convert()
background = pygame.transform.scale(background, screen.get_size())

floor_img = pygame.image.load(floor_path).convert_alpha()
floor_height = floor_img.get_height()
floor_img = pygame.transform.scale(floor_img, (screen.get_width(), floor_height))
floor_y = screen.get_height() - floor_img.get_height()

pipe_img = pygame.image.load(pipe_path).convert_alpha()
pipe_top_img = pygame.transform.flip(pipe_img, False, True)
pipe_w, pipe_h = pipe_img.get_size()

PIPE_GAP = 160
PIPE_SPEED = 3
PIPE_SPAWN_MS = 1400

pipes = []
last_pipe_spawn_ms = pygame.time.get_ticks()

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel_y = -10.0
            if event.key == pygame.K_ESCAPE:
                running = False

    now_ms = pygame.time.get_ticks()
    if now_ms - last_pipe_spawn_ms >= PIPE_SPAWN_MS:
        min_gap_y = 50
        max_gap_y = floor_y - 50 - PIPE_GAP
        if max_gap_y > min_gap_y:
            gap_y = random.randint(int(min_gap_y), int(max_gap_y))
            pipes.append({"x": screen.get_width() + 20, "gap_y": gap_y})
        last_pipe_spawn_ms = now_ms

    for pipe in pipes:
        pipe["x"] -= PIPE_SPEED
    pipes = [p for p in pipes if p["x"] + pipe_w > 0]

    bird_vel_y += gravity
    bird_y += bird_vel_y
    if bird_y + bird_h >= floor_y:
        bird_y = floor_y - bird_h
        bird_vel_y = 0.0

    screen.blit(background, (0, 0))
    for pipe in pipes:
        top_y = pipe["gap_y"] - pipe_h
        bottom_y = pipe["gap_y"] + PIPE_GAP
        screen.blit(pipe_top_img, (pipe["x"], top_y))
        screen.blit(pipe_img, (pipe["x"], bottom_y))
    screen.blit(bird_img, (bird_x, bird_y))
    screen.blit(floor_img, (0, floor_y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()