import pygame
import random

pygame.init()

# Colours
tur = (0, 205, 205)
white = (255, 255,255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (34, 139, 34)

screen_width = 900
screen_height = 600
# Creating window for game
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Setting Title
pygame.display.set_caption("Hungry Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.Font("C:\Windows\Fonts\ka1.ttf", 45)

def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, colour, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, colour, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((0,205,205))
        text_screen("Welcome to Snakes", black, 130, 200)
        text_screen("Press Space Bar to play", black, 50, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(60)

# Game loop
def game_loop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    velocity_x = 0
    velocity_y = 0

    snake_list = []
    snake_length = 1

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(50, screen_width - 50)
    food_y = random.randint(70, screen_height - 50)
    score = 0
    init_velocity = 5

    fps = 40

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(tur)
            text_screen("Game Over!", black, 270, 220)
            text_screen("Press Enter To Continue", black, 60, 270)

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
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 10
                food_x = random.randint(50, screen_width - 50)
                food_y = random.randint(70, screen_height - 50)
                snake_length += 5
                if score>int(highscore):
                    highscore = score

            # The initial body 
            head = []                                      
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            
            # Control of snake length
            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height :
                game_over = True
                print("Game Over!")

            gameWindow.fill(white)
            text_screen("Score: " + str(score) + "  High Score:" + str(highscore), black, 5, 5)
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, green, snake_list, snake_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()
game_loop()
