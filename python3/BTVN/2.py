import pygame
import random
import time
import math

pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple RPG")

# Player
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 1
player_color = GREEN

# Apple
apple_x = random.randint(0, WIDTH)
apple_y = random.randint(0, HEIGHT)
apple_color = RED

# Golden Apple
golden_apple_x = -100  # Start off-screen
golden_apple_y = -100
golden_apple_color = YELLOW
golden_apple_timer = 0
golden_apple_respawn_time = 15  # Respawn time in seconds

# Score
score = 0
font = pygame.font.Font(None, 36)

# Timer
start_time = time.time()
timer = 60  # Timer in seconds

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Normalize diagonal movement
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        player_x -= player_speed / math.sqrt(2)
        player_y -= player_speed / math.sqrt(2)
    elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        player_x += player_speed / math.sqrt(2)
        player_y -= player_speed / math.sqrt(2)
    elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        player_x -= player_speed / math.sqrt(2)
        player_y += player_speed / math.sqrt(2)
    elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        player_x += player_speed / math.sqrt(2)
        player_y += player_speed / math.sqrt(2)

    # Check for Apple Collision
    if (
        player_x < apple_x + 20
        and player_x + 20 > apple_x
        and player_y < apple_y + 20
        and player_y + 20 > apple_y
    ):
        score += 1
        apple_x = random.randint(0, WIDTH)
        apple_y = random.randint(0, HEIGHT)

    # Check for Golden Apple Collision
    if (
        player_x < golden_apple_x + 20
        and player_x + 20 > golden_apple_x
        and player_y < golden_apple_y + 20
        and player_y + 20 > golden_apple_y
    ):
        score += 3
        golden_apple_x = -100
        golden_apple_y = -100
        golden_apple_timer = time.time()  # Reset timer for respawn

    # Golden Apple Timer
    if time.time() - golden_apple_timer >= 5:  # 5 seconds to appear
        if golden_apple_x == -100:  # Only spawn if not already on screen
            golden_apple_x = random.randint(0, WIDTH)
            golden_apple_y = random.randint(0, HEIGHT)

    # Update Timer
    elapsed_time = time.time() - start_time
    timer = 60 - int(elapsed_time)

    # Stop the game when the timer hits 0
    if timer <= 0:
        running = False

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, player_color, (player_x, player_y, 20, 20))
    pygame.draw.circle(screen, apple_color, (apple_x, apple_y), 10)

    if golden_apple_x != -100:
        pygame.draw.circle(screen, golden_apple_color, (golden_apple_x, golden_apple_y), 10)

    # Display Score and Timer
    score_text = font.render(f"Score: {score}", True, BLACK)
    timer_text = font.render(f"Time: {timer}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (WIDTH - timer_text.get_width() - 10, 10))

    pygame.display.flip()

pygame.quit()