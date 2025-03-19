import pygame
import sys
from datetime import datetime

DARK = (160, 160, 160)
WHITE = (255, 255, 255)
pygame.init()
SIZE = 1500
CENTER = (SIZE // 2 -350 , SIZE // 2 -393)
window = pygame.display.set_mode((SIZE, SIZE))
clock = pygame.time.Clock()

class Button:
    def __init__(self, x, y, width, height, text, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.color = (200, 200, 200)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, event):
        return event.type==pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

def draw_hand(surface, image, angle):
    a = 0.75
    photo1 = (int(image.get_width() * a), int(image.get_height() * a))
    photo2 = pygame.transform.scale(image,photo1)

    photo =pygame.transform.rotate(photo2, -angle)
    rect =photo.get_rect(center=CENTER)
    surface.blit(photo, rect)

def run():
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Micky Broski")
   
    background = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab7/clock(4).png")  
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  

    minute_hand_img = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab7/larm.png")
    second_hand_img = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab7/rarm"
    ".png")

    pygame.mixer.init()
    pygame.mixer.music.load('/Users/kuanyshev11/Documents/zhanibek/labs/lab7/bober.mp3')   
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  

    running = True
    music_paused = False
   
    while running:
        screen.blit(background, (0, 0))
        now = datetime.now()

        draw_hand(screen, minute_hand_img, now.minute * 6)
        draw_hand(screen, second_hand_img, now.second * 6)

        pygame.display.flip()

run()
