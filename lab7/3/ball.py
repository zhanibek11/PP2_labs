import pygame
pygame.init()

a, b = 800, 600  
c = pygame.display.set_mode((a, b))  
pygame.display.set_caption("Ball Game")

# Шарик
d = pygame.Color('red')
e = pygame.Color('white')
f = [a // 2, b // 2]
g = 25  
h = 20  

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys= pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        f[1]= max(f[1] - h, g)
    if keys[pygame.K_DOWN]:
        f[1] = min(f[1] + h, b - g)
    if keys[pygame.K_LEFT]:
        f[0] = max(f[0] - h, g)
    if keys[pygame.K_RIGHT]:
        f[0] =min(f[0] + h, a - g)
    
    c.fill(e)
    pygame.draw.circle(c, d,  f, g)
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()