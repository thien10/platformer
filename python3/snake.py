import pygame, sys, random
from pygame import draw
from pygame.locals import QUIT

pygame.init()

red = (255, 0, 0)
blue = (1, 53, 143)
white = (255, 255, 255)
green = (147, 232, 67)
l_green = (169, 245, 98)
d_green = (36, 135, 0)
yellow = (255, 196, 0)
gray = (79, 78, 73)
brown = (201, 130, 54)
black = (0, 0, 0)

screen_x = 600
screen_y = 400
DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y))

snake_block = 20
font = pygame.font.Font(None, 36)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake_x = 300
snake_y = 200
snake_dx = 0
snake_dy = 0
snake_length = 1
snake_coords = []

last_direction = None

best_scores = {
    1: 0,  # Classic
    2: 0,  # Block
    3: 0,  # Key
    4: 0,  # Box
}

try:
    with open("best_score.txt", "r") as file:
        for line in file:
            mode, score = line.strip().split(":")
            best_scores[int(mode)] = int(score)
except FileNotFoundError:
    pass

def generate_coords(snake_coords):
    while True:
        x = random.randint(1, 59) * snake_block
        y = random.randint(1, 39) * snake_block
        if (x, y) not in snake_coords and 0 <= x < screen_x and 0 <= y < screen_y:
            break
    return x, y

def reset_objects():
    global food_x, food_y, block_x, block_y, key_x, key_y, box_x, box_y, key_obtained, food_unlocked
    food_x, food_y = generate_coords(snake_coords)
    block_x, block_y = generate_coords(snake_coords)
    key_x, key_y = generate_coords(snake_coords)
    box_x, box_y = generate_coords(snake_coords)
    key_obtained = False
    food_unlocked = False

def check_game_over():
    if gamemode == 2 and block_x == snake_x and block_y == snake_y:
        return True

def check_food(gamemode):
    global snake_length, key_obtained, food_unlocked
    if gamemode == 1 or gamemode == 2:
        snake_length += 1
    elif gamemode == 3 and key_obtained:
        snake_length += 1
        key_obtained = False
    elif gamemode == 4 and food_unlocked:
        snake_length += 1
        food_unlocked = False

def draw_bg():
    for i in range(int(screen_x / 20)):
        for j in range(int(screen_y / 20)):
            if (i + j) % 2 == 0:
                pygame.draw.rect(DISPLAYSURF, l_green, (i * 20, j * 20, 20, 20))
            else:
                pygame.draw.rect(DISPLAYSURF, green, (i * 20, j * 20, 20, 20))

def snake(snake_block, snake_coords):
    for coord in snake_coords:
        pygame.draw.rect(DISPLAYSURF, blue, (coord[0], coord[1], snake_block, snake_block))

def menu_screen():
    global gamemode
    draw_bg()
    game_options = ['Classic', 'Block', 'Key', 'Box']
    option = 0  
    while True:
        title_text = font.render('Snake Game', True, black)
        title_rect = title_text.get_rect(center=(screen_x//2, screen_y//3))
        DISPLAYSURF.blit(title_text, title_rect)
        for i, option_text in enumerate(game_options):
            text = font.render(option_text, True, black if i == option else gray)
            text_rect = text.get_rect(center=(screen_x // 2, (screen_y // 3) + (i + 1) * 50))
            DISPLAYSURF.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    option = (option - 1) % len(game_options)
                elif event.key == pygame.K_DOWN:
                    option = (option + 1) % len(game_options)
                elif event.key == pygame.K_RETURN:
                    gamemode = option + 1
                    return gamemode  
        pygame.display.update()
        clock.tick(10)

def leaderboard_screen():
    global best_score, gamemode
    draw_bg()
    leaderboard_text = font.render('Leaderboard', True, black)
    leaderboard_rect = leaderboard_text.get_rect(center=(screen_x // 2, screen_y // 3))
    DISPLAYSURF.blit(leaderboard_text, leaderboard_rect)
    best_score_text = font.render(f'Best Score: {best_scores[gamemode]}', True, black)
    best_score_rect = best_score_text.get_rect(center=(screen_x // 2, (screen_y // 3) + 50))
    DISPLAYSURF.blit(best_score_text, best_score_rect)
    back_text = font.render('Back', True, black)
    back_rect = back_text.get_rect(center=(screen_x // 2, (screen_y // 3) + 100))
    DISPLAYSURF.blit(back_text, back_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gamemode = 0  # Return to the menu
                    return
        pygame.display.update()
        clock.tick(10)

while True:
    snake_coords = [[snake_x, snake_y]] 
    food_x, food_y = generate_coords(snake_coords)
    block_x, block_y = generate_coords(snake_coords)
    key_x, key_y = generate_coords(snake_coords)
    box_x, box_y = generate_coords(snake_coords)
    box_dx = 0
    box_dy = 0
    key_obtained = False
    food_unlocked = False
    gamemode = menu_screen()
    gamemode_highscore = 0


    while True:
         
        if gamemode == 0:
            gamemode = menu_screen()  
            snake_coords.clear()
            snake_length = 1
            snake_x = 300
            snake_y = 200
            snake_dx = 0
            snake_dy = 0
            last_direction = None
            reset_objects()

        snake_x += snake_dx
        snake_y += snake_dy

        if gamemode == 4:
            if (snake_x == box_x and snake_y == box_y):
                box_x += snake_dx
                box_y += snake_dy
                if box_x < 0 or box_x >= screen_x or box_y < 0 or box_y >= screen_y:
                    box_x, box_y = generate_coords(snake_coords)

        if food_x == snake_x and food_y == snake_y:
            check_food(gamemode)
            reset_objects()

        if check_game_over():
            print('Game Over! Your score is:', len(snake_coords))
            leaderboard_screen()  # Show the leaderboard
            gamemode = 0  # Go back to the menu
            break

        if gamemode == 3:
            if key_x == snake_x and key_y == snake_y:
                key_obtained = True
        if gamemode == 4:
            if box_x == food_x and box_y == food_y:
                food_unlocked = True

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_direction != "right":
                    snake_dx = -snake_block
                    snake_dy = 0
                    last_direction = "left"
                elif event.key == pygame.K_RIGHT and last_direction != "left":
                    snake_dx = snake_block
                    snake_dy = 0
                    last_direction = "right"
                elif event.key == pygame.K_UP and last_direction != "down":
                    snake_dx = 0
                    snake_dy = -snake_block
                    last_direction = "up"
                elif event.key == pygame.K_DOWN and last_direction != "up":
                    snake_dx = 0
                    snake_dy = snake_block
                    last_direction = "down"
                continue

        draw_bg()
        snake_head = [snake_x, snake_y]
        snake_coords.append(snake_head)

        if len(snake_coords) > snake_length:
            del snake_coords[0]

        snake(snake_block, snake_coords)
        pygame.draw.rect(DISPLAYSURF, red, (food_x, food_y, snake_block, snake_block))

        if gamemode == 2:
            pygame.draw.rect(DISPLAYSURF, d_green, (block_x, block_y, snake_block, snake_block))

        if gamemode == 3:
            if key_obtained:
                pygame.draw.rect(DISPLAYSURF, red, (food_x, food_y, snake_block, snake_block))
            else:
                pygame.draw.rect(DISPLAYSURF, gray, (food_x, food_y, snake_block, snake_block))

            if not key_obtained:
                pygame.draw.rect(DISPLAYSURF, yellow, (key_x, key_y, snake_block, snake_block))

        if gamemode == 4:
            if food_unlocked:
                pygame.draw.rect(DISPLAYSURF, red, (food_x, food_y, snake_block, snake_block))
            else:
                pygame.draw.rect(DISPLAYSURF, gray, (food_x, food_y, snake_block, snake_block))
            pygame.draw.rect(DISPLAYSURF, brown, (box_x, box_y, snake_block, snake_block))

        score_text = font.render(f"Score: {snake_length}", True, black)
        DISPLAYSURF.blit(score_text, (10, 10))

        best_score_text = font.render(f"Best: {best_scores[gamemode]}", True, black)
        DISPLAYSURF.blit(best_score_text, (screen_x - best_score_text.get_width() - 10, 10))

        if len(snake_coords) > 1:  # Collision check AFTER snake moves
            for coord in snake_coords[:-1]:
                snake_head = snake_coords[-1]
                if coord == snake_head:
                    print('Game Over! Your score is:', len(snake_coords))
                    leaderboard_screen()  # Show the leaderboard
                    gamemode = 0  # Go back to the menu
                    break

        if snake_coords:  # Border collision check AFTER snake moves
            snake_head = snake_coords[-1]
            if (snake_head[0] >= screen_x or snake_head[0] < 0) or (snake_head[1] >= screen_y or snake_head[1] < 0):
                print('Game Over! Your score is:', len(snake_coords))
                leaderboard_screen()  # Show the leaderboard
                gamemode = 0  # Go back to the menu
                break

        if snake_length > best_scores[gamemode]:
            best_scores[gamemode] = snake_length
            with open("best_score.txt", "w") as file:
                for mode, score in best_scores.items():
                    file.write(f"{mode}:{score}\n")
            with open("best_score.txt", "r") as file:  # Open the file again in read mode ("r")
                a = file.readlines()  # Read all lines
            print(a)  # Print the list of lines

        pygame.display.update()
        clock.tick(5)