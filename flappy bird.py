import pygame
import time
import random
from pygame import mixer

pygame.init()
song = "death bed.mp3"
mixer.music.load(song)
mixer.music.play(-1)
time.music = -1

screen = pygame.display.set_mode((300, 500))
background_image = pygame.image.load("back_grou_ndd.jpg")
bird_image = pygame.image.load("bird.png")
bird_x = 20
bird_y = 270
bird_y_change = 0

# pipe
pipe_width = 70
pipe_height = random.randint(170, 300)
pipe_color = (211, 253, 117)
pipe_x_change = -4
pipe_x = 300


def display_pipe(height):
    pygame.draw.rect(screen, pipe_color, (pipe_x, 0, pipe_width, pipe_height))
    bottom_pipe_height = 380 - height - 200
    pygame.draw.rect(screen, pipe_color, (pipe_x, 380, pipe_width, -bottom_pipe_height))


def display_bird(x, y):
    screen.blit(bird_image, (x, y))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -0.4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 0.2

    pipe_x += pipe_x_change
    if pipe_x <= -2000:
        pipe_x = 1000
        pipe_height = random.randint(150, 300)
        bottom_pipe_height = random.randint(5000, 8000)
    display_pipe(pipe_height)

    bird_y += bird_y_change
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 380:
        bird_y = 380

    display_bird(bird_x, bird_y)

    pygame.display.update()
pygame.quit()
