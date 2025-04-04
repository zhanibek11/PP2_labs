import pygame
import sys
import math

# запускаю пайгейм и создаю окно
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('simple paint')

# настраиваю цвета
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# переменные для рисования
drawing = False
brush_color = black
shape = "brush"

# класс для кнопок
class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action
    
    # рисую кнопку
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 5))
    
    # проверяю нажата ли кнопка
    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

# функции для смены цвета
def set_black():
    global brush_color
    brush_color = black

def set_green():
    global brush_color
    brush_color = green

def set_red():
    global brush_color
    brush_color = red

def set_blue():
    global brush_color
    brush_color = blue

def set_eraser():
    global brush_color
    brush_color = white

# очистка экрана
def clear_screen():
    screen.fill(white)

# выход из приложения
def exit_app():
    pygame.quit()
    sys.exit()

# выбор инструментов
def set_brush():
    global shape
    shape = "brush"

def set_circle():
    global shape
    shape = "circle"

def set_rectangle():
    global shape
    shape = "rectangle"

def set_square():
    global shape
    shape = "square"

def set_right_triangle():
    global shape
    shape = "right_triangle"

def set_equilateral_triangle():
    global shape
    shape = "equilateral_triangle"

def set_rhombus():
    global shape
    shape = "rhombus"

# создаю кнопки
buttons = [
    Button(10, 10, 60, 30, "Black", black, set_black),
    Button(80, 10, 60, 30, "Green", green, set_green),
    Button(150, 10, 60, 30, "Red", red, set_red),
    Button(220, 10, 60, 30, "Blue", blue, set_blue),
    Button(290, 10, 60, 30, "Eraser", gray, set_eraser),
    Button(360, 10, 60, 30, "Brush", gray, set_brush),
    Button(430, 10, 60, 30, "Circle", gray, set_circle),
    Button(500, 10, 60, 30, "Rect", gray, set_rectangle),
    Button(570, 10, 60, 30, "Square", gray, set_square),
    Button(640, 10, 60, 30, "Right", gray, set_right_triangle),
    Button(710, 10, 60, 30, "EqTri", gray, set_equilateral_triangle),
    Button(10, 50, 60, 30, "Rhomb", gray, set_rhombus),
    Button(80, 50, 60, 30, "Clear", gray, clear_screen),
    Button(150, 50, 60, 30, "Exit", gray, exit_app)
]

# заливаю фон белым
clear_screen()
start_pos = None

# основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # нажал кнопку мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = pygame.mouse.get_pos()
                for button in buttons:
                    button.check_click(event)
        
        # отпустил кнопку мыши
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = pygame.mouse.get_pos()
                x1, y1 = start_pos
                x2, y2 = end_pos
                if shape == "rectangle":
                    pygame.draw.rect(screen, brush_color, (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)))
                elif shape == "circle":
                    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                    pygame.draw.circle(screen, brush_color, start_pos, radius)
                elif shape == "square":
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(screen, brush_color, (x1, y1, side, side))
                elif shape == "right_triangle":
                    pygame.draw.polygon(screen, brush_color, [start_pos, (x1, y2), (x2, y2)])
                elif shape == "equilateral_triangle":
                    height_eq = (3 ** 0.5 / 2) * abs(x2 - x1)
                    pygame.draw.polygon(screen, brush_color, [
                        ((x1 + x2) // 2, y1),
                        (x1, y1 + int(height_eq)),
                        (x2, y1 + int(height_eq))
                    ])
                elif shape == "rhombus":
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    dx = abs(x2 - x1) // 2
                    dy = abs(y2 - y1) // 2
                    pygame.draw.polygon(screen, brush_color, [
                        (center_x, y1),
                        (x2, center_y),
                        (center_x, y2),
                        (x1, center_y)
                    ])
                start_pos = None

    # если рисую кистью, то просто ставлю кружочки
    if drawing and shape == "brush":
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 90:
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)

    # рисую панель и кнопки
    pygame.draw.rect(screen, gray, (0, 0, width, 90))
    for button in buttons:
        button.draw(screen)
    
    pygame.display.flip()