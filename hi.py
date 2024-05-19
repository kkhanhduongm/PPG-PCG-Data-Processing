import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 400
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flappy Bird")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the bird
bird_width = 50
bird_height = 50
bird_x = 50
bird_y = window_height // 2 - bird_height // 2
bird_speed = 0
gravity = 1
jump_height = -15

# Set up the pipes
pipe_width = 80
pipe_gap = 150
pipe_speed = 3
pipe_x = window_width
pipe_height = random.randint(100, 300)
pipe_y_top = pipe_height
pipe_y_bottom = pipe_height + pipe_gap

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_speed = jump_height
            if event.key == pygame.K_r and game_over:
                # Reset the game
                bird_y = window_height // 2 - bird_height // 2
                bird_speed = 0
                pipe_x = window_width
                score = 0
                game_over = False

    if not game_over:
        # Move the bird
        bird_speed += gravity
        bird_y += bird_speed

        # Move the pipes
        pipe_x -= pipe_speed

        # Check for collision with the pipes
        if bird_x + bird_width > pipe_x and bird_x < pipe_x + pipe_width:
            if bird_y < pipe_y_top or bird_y + bird_height > pipe_y_bottom:
                game_over = True

        # Check if the pipe has passed the bird
        if pipe_x + pipe_width < bird_x:
            score += 1
            pipe_x = window_width
            pipe_height = random.randint(100, 300)
            pipe_y_top = pipe_height
            pipe_y_bottom = pipe_height + pipe_gap

        # Check for collision with the ground or ceiling
        if bird_y + bird_height > window_height or bird_y < 0:
            game_over = True

    # Draw the background
    window.fill(black)

    # Draw the bird
    pygame.draw.rect(window, white, (bird_x, bird_y, bird_width, bird_height))

    # Draw the pipes
    pygame.draw.rect(window, white, (pipe_x, 0, pipe_width, pipe_y_top))
    pygame.draw.rect(window, white, (pipe_x, pipe_y_bottom, pipe_width, window_height - pipe_y_bottom))

    # Draw the score
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render("Game Over! Press 'R' to Restart", True, white)
        window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
