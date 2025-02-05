import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Display dimensions
WIDTH = 600
HEIGHT = 400

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
# Clock and game speed
clock = pygame.time.Clock()
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Fonts for score and messages
score_font = pygame.font.SysFont("comicsansms", 35)
message_font = pygame.font.SysFont("bahnschrift", 25)

def show_score(score):
    """Display the current score."""
    value = score_font.render("Score: " + str(score), True, BLUE)
    screen.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

def display_message(msg, color):
    """Display a centered message on the screen."""
    mesg = message_font.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    # Starting position of the snake's head
    x = WIDTH / 2
    y = HEIGHT / 2

    # Change in position (velocity)
    x_change = 0
    y_change = 0

    # Snake list and initial length
    snake_list = []
    snake_length = 1

    # Generate first food position
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            display_message("You lost! Press C-Play Again or Q-Quit", RED)
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        # Check for collision with boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Update snake head position
        x += x_change
        y += y_change
        screen.fill(BLACK)
        
        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
        
        # Update snake's body list
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with self
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        show_score(snake_length - 1)
        pygame.display.update()

        # Check if snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
