import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# просто цвета
BLUE = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK =(0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH=600
SCREEN_HEIGHT=600

DISPLAYSURF= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

font = pygame.font.Font(None, 36)
game_over_font =pygame.font.Font(None, 72)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab8/grandma.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = 10  # скорость врага

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab8/mrbean.png")
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1,2,3])  # вес монеты, случайный выбор
        self.image = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab8/teddy.png")
        size = 30 + self.weight * 10  # чем больше вес, тем больше размер
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = 7

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.__init__()  # пересоздаём монету с новым весом

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# создаём игрока, врага и первую монету
P1 = Player()
E1 = Enemy()
coin = Coin()

score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()
    coin.move()

    if P1.rect.colliderect(coin.rect):
        score += coin.weight  # добавляем очки по весу монеты
        coin = Coin()         # создаём новую монету

        # если заработали много очков, ускоряем врага
        if score % 5 == 0:
            E1.speed += 1

    if P1.rect.colliderect(E1.rect):
        running = False

    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    coin.draw(DISPLAYSURF)

    score_text = font.render(f"Coins: {score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (SCREEN_WIDTH - 150, 20))

    pygame.display.update()
    FramePerSec.tick(FPS)

# проиграли, показываем game over
DISPLAYSURF.fill(BLACK)
game_over_text = game_over_font.render("GAME OVER", True, RED)
game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
DISPLAYSURF.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()
sys.exit()
