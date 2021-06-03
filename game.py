import pygame
import random
pygame.init()

# Define colors and screen size
white = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
yellow = (255, 255, 0)
Purple = (128, 0, 128)
maroon = (128, 0, 0)

# Define screen size and clock
screen_height = 600
screen_width = 600
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
img = pygame.image.load("tree.png")

gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Snake Game")
img = pygame.image.load("tree.png")
bgimg = pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()
pygame.display.update()

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(bgimg, (0, 0))
        text_screen("Welcome to My Snake Game", Purple, 70, 180)
        text_screen("Press Space to Start", Purple, 140, 270)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
        pygame.display.update()
        clock.tick(60)

def plot_snake(gamewindow, color, snake_lst, snake_size):
    for x, y in snake_lst:
        pygame.draw.rect(gamewindow, red, [x, y, snake_size, snake_size])
    pygame.draw.rect(gamewindow, maroon, [x, y, snake_size, snake_size])
    
def game_loop():
    # specific variables
    exit_game = False
    game_over = False
    snake_size = 20
    snake_x = 40
    snake_y = 40
    velocity_x = 5
    velocity_y = 5
    snake_lst = []
    snake_length = 1
    food_x = random.randint(20, screen_width-20)
    food_y = random.randint(50, screen_height-20)
    score = 0

    while not exit_game:
        if game_over == True:
            gamewindow.fill(green)
            text_screen("Game Over!", red, 200, 150)
            text_screen("Score: " + str(score), red, 230, 200)
            text_screen("Press Enter to Play again", red, 100, 300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -5
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 5
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y
            
            if abs(snake_x - food_x) < 20  and abs(snake_y - food_y) < 20:
                score += 10
                food_x = random.randint(20, screen_width-20)
                food_y = random.randint(50, screen_height-20)
                snake_length += 10

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_lst.append(head)

            if len(snake_lst) > snake_length:
                del snake_lst[0]

            if head in snake_lst[:-1]:
                game_over = True

            if (snake_x <= 0 or snake_x >= screen_width-20 or snake_y <= 0 or snake_y >= screen_height-20):
                game_over = True
                
            gamewindow.fill(green)
            plot_snake(gamewindow, red, snake_lst, snake_size)
            pygame.draw.circle(gamewindow, yellow, (food_x, food_y), 10)
            text_screen("Score: "+ str(score), Purple, 5, 5)
        pygame.display.update()
        clock.tick(30)
    
    pygame.quit()
    quit()

welcome()

