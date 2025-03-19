import pygame
import pygame.gfxdraw
from datetime import datetime

dark_grey = (160,160,160)
white = (255,255,255)
color = (122,122,122)

pygame.init()
size = 400
center = (size//2, size//2)

window = pygame.display.set_mode((size,size))
clock = pygame.time.Clock()

def draw_second_hand(surface, second):
    hand_length = size * 0.4
    angle = second * 6
    end_x = center[0] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).x
    end_y = center[1] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).y
    pygame.draw.line(surface, dark_grey, center , (end_x, end_y), 5)
def draw_minute_hand(surface, minute):
    hand_length = size * 0.3
    angle = minute * 6
    end_x = center[0] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).x
    end_y = center[1] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).y
    pygame.draw.line(surface, color, center , (end_x, end_y), 7)
def main():
    running = True
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Hala Madrid")
   
    background = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab7/image.jpg")  
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    while running:
        pygame.init()
        window.fill(white)
        now = datetime.now()
        draw_second_hand(window, now.second)
        draw_minute_hand(window,now.minute)
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    
    pygame.quit()


main()