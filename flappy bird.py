import pygame
import random
from pygame import mixer

pygame.init()
song = "death bed.mp3"
mixer.music.load(song)
mixer.music.play(-1)  # Play the music in an infinite loop

screen = pygame.display.set_mode((300, 500))
background_image = pygame.image.load("back_grou_ndd.jpg")
bird_image = pygame.image.load("bird.png")
bird_x = 20
bird_y = 270
bird_y_change = 0

# Pipe
pipe_width = 70
pipe_color = (211, 253, 117)
pipe_x_change = -2
pipes = []
initial_pipe_x = 300
pipe_spacing = 100
pipe_height = 250  # Fixed pipe height
pipe_distance = 200  # Distance between the pipes

def create_pipe():
    random_height = random.randint(150, 300)
    top_pipe = pygame.Rect(initial_pipe_x, 0, pipe_width, random_height)
    bottom_pipe = pygame.Rect(initial_pipe_x, random_height + pipe_spacing, pipe_width, 500)
    return top_pipe, bottom_pipe

def display_pipe(top_pipe, bottom_pipe):
    pygame.draw.rect(screen, pipe_color, top_pipe)
    pygame.draw.rect(screen, pipe_color, bottom_pipe)

def display_bird(x, y):
    screen.blit(bird_image, (x, y))

def move_pipes():
    for top_pipe, bottom_pipe in pipes:
        top_pipe.x += pipe_x_change
        bottom_pipe.x += pipe_x_change

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 2

    bird_y += bird_y_change
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 380:
        bird_y = 380

    move_pipes()

    for top_pipe, bottom_pipe in pipes:
        display_pipe(top_pipe, bottom_pipe)

        bird_rect = bird_image.get_rect(x=bird_x, y=bird_y)
        if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
            running = False  # End the game when the bird collides with any pipe

    display_bird(bird_x, bird_y)

    if len(pipes) > 0 and pipes[0][0].x <= -pipe_width:
        pipes.pop(0)  # Remove pipes that have gone off-screen

    if len(pipes) == 0 or screen.get_width() - pipes[-1][0].x > pipe_distance:  # Distance between pipes
        pipes.append(create_pipe())

    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 frames per second

pygame.quit()
