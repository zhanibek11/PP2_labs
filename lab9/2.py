import pygame 
import sys 
import random
import time

# запускаем pygame
pygame.init()

# задаем размер экрана и клетки
width, height = 500, 500
cell_size = 10

# создаем окно игры
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("simple snake")

# цвета для фона, змейки и еды
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# начальная позиция головы змейки
snake_pos = [100, 100]

# тело змейки — список клеток
snake_body = [[100, 100], [90, 100], [80, 100]]

# направление движения
direction = "RIGHT"
change_to = direction

# стартовая скорость, очки и уровень
speed = 10
score = 0
level = 1

# список для еды (чтоб можно было несколько штук сразу)
foods = []

# функция чтобы создать новую еду
def generate_food():
    while True:
        x = random.randrange(0, width, cell_size)
        y = random.randrange(0, height, cell_size)
        pos = [x, y]
        if pos not in snake_body:
            # вес еды от 1 до 3
            weight = random.randint(1, 3)
            # таймер жизни еды — через сколько секунд исчезнет
            ttl = time.time() + random.randint(5, 10)
            return {"pos": pos, "weight": weight, "ttl": ttl}

# сначала кидаем одну еду
foods.append(generate_food())

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
    
    # обновляем направление
    direction = change_to

    # двигаем голову змейки
    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size
    
    # проверка на выход за границы
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False
    
    # проверка на столкновение с собой
    if snake_pos in snake_body[1:]:
        running = False

    # добавляем новую голову
    snake_body.insert(0, list(snake_pos))

    # флаг, съел ли змейка еду
    ate = False

    # проходим по еде
    for food in foods:
        if snake_pos == food["pos"]:
            score += food["weight"]  # прибавляем очки в зависимости от веса
            ate = True
            foods.remove(food)
            break
    
    if not ate:
        snake_body.pop()  # если еду не съели — хвост укорачиваем

    # иногда (рандомно) добавляем новую еду
    if len(foods) < 3 and random.randint(0, 50) == 0:
        foods.append(generate_food())

    # удаляем еду, если прошло её время
    now = time.time()
    foods = [f for f in foods if f["ttl"] > now]

    # увеличиваем уровень каждые 4 очка
    if score // 4 + 1 > level:
        level += 1
        speed += 2

    # очищаем экран
    screen.fill(black)

    # рисуем змейку
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    
    # рисуем еду — цвет зависит от веса
    for food in foods:
        color = (255, 100, 100) if food["weight"] == 1 else (255, 150, 0) if food["weight"] == 2 else (255, 255, 0)
        pygame.draw.rect(screen, color, pygame.Rect(food["pos"][0], food["pos"][1], cell_size, cell_size))
    
    # отображаем счет и уровень
    font = pygame.font.Font(None, 24)
    score_text = font.render(f'score: {score}  level: {level}', True, white)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()