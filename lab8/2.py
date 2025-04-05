import pygame 
import sys 
import random

# инициализация Pygame
pygame.init()

# параметры экрана
width, height = 500, 500
cell_size = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Snake")

# цвета
white =(255, 255, 255)
black =(0, 0, 0)
green =(0, 255, 0)
red =(255, 0, 0)

# начальные параметры змейки
snake_pos = [100, 100]
snake_body = [[100, 100], [90, 100], [80, 100]]

direction = "RIGHT"
change_to = direction

# изначальная скорость и счетчик очков
speed = 10
score = 0
level = 1

# функция генерации еды так, чтобы она не попала на змейку

def generate_food():
    while True:
        food = [random.randrange(0, width, cell_size), random.randrange(0, height, cell_size)]
        if food not in snake_body:  # Проверяем, чтобы еда не была на змейке
            return food

food_pos = generate_food()

clock = pygame.time.Clock()
running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN": 
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = 'RIGHT'
    
    direction = change_to  # обновляем направление движения змейки

    # обновляем позицию головы змейки
    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size
    
    # проверяем столкновение со стенами
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False  # если вышли за границы — конец игры
    
    # проверяем столкновение с самой собой
    if snake_pos in snake_body[1:]:
        running = False  # если голова змейки врезалась в тело — конец игры

    # добавляем новую голову змейки
    snake_body.insert(0, list(snake_pos))
    
    # проверяем, съела ли змейка еду
    if snake_pos == food_pos:
        score += 1  # увеличиваем счет
        food_pos = generate_food()  # генерируем новую еду
        # увеличиваем уровень каждые 4 еды
        if score % 4 == 0:
            level += 1
            speed += 2  # увеличиваем скорость
    else:
        snake_body.pop()  #если не съела — убираем хвост

    #обновляем экран
    screen.fill(black)
    
    # рисуем змейку
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    
    #рисуем еду
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))
    
    # отображаем счетчик очков и уровень
    font = pygame.font.Font(None, 24)
    score_text = font.render(f'Score: {score}  Level: {level}', True, white)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)  # управляем скоростью змейки

pygame.quit()
sys.exit()
