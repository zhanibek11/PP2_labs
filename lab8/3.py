import pygame
import sys

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Paint')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

drawing = False
brush_color = black
shape = "brush"

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 5))
    
    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

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

def clear_screen():
    screen.fill(white)

def exit_app():
    pygame.quit()
    sys.exit()

def set_brush():
    global shape
    shape = "brush"

def set_circle():
    global shape
    shape = "circle"

def set_rectangle():
    global shape
    shape = "rectangle"

buttons = [
    Button(10, 10, 60, 30, "Black", black, set_black),
    Button(80, 10, 60, 30, "Green", green, set_green),
    Button(150, 10, 60, 30, "Red", red, set_red),
    Button(220, 10, 60, 30, "Blue", blue, set_blue),
    Button(290, 10, 60, 30, "Eraser", gray, set_eraser),
    Button(360, 10, 60, 30, "Brush", gray, set_brush),
    Button(430, 10, 60, 30, "Circle", gray, set_circle),
    Button(500, 10, 60, 30, "Rect", gray, set_rectangle),
    Button(570, 10, 60, 30, "Clear", gray, clear_screen),
    Button(640, 10, 60, 30, "Exit", gray, exit_app)
]

clear_screen()
start_pos = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = pygame.mouse.get_pos()
                for button in buttons:
                    button.check_click(event)
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = pygame.mouse.get_pos()
                if shape == "rectangle" and start_pos:
                    pygame.draw.rect(screen, brush_color, (min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1])))
                if shape == "circle" and start_pos:
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, brush_color, start_pos, radius)
                start_pos = None
        
    if drawing and shape == "brush":
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 50:
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)
    
    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)
    
    pygame.display.flip()
