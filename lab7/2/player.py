import pygame
import os 

pygame.init()

musiclist = []
folder = "/Users/kuanyshev11/Documents/zhanibek/labs/lab7/2/musicashere"
musicas = os.listdir(folder)

for song in musicas:
    if song.endswith(".mp3"):
        musiclist.append(os.path.join(folder,song))

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Dean-Martin")
clock = pygame.time.Clock()

background = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab7/2/kuanyshev/back.png")

bg = pygame.Surface((500,200))
bg.fill((255,255,255))

font2 = pygame.font.SysFont(None,20)

playbut = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab7/2/kuanyshev/pl.png")
pausebut = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab7/2/kuanyshev/pau.png")
nextbut = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab7/2/kuanyshev/nex.png")
prevbut = pygame.image.load("/Users/kuanyshev11/Documents/zhanibek/labs/lab7/2/kuanyshev/prev.png")

index = 0
aplay = False

pygame.mixer.music.load(musiclist[index])
pygame.mixer.music.play(1)
aplay = True

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                if aplay:
                    aplay =  False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()
            
            if event.key == pygame.K_RIGHT:
                index = (index+1)%len(musiclist)
                pygame.mixer.music.load(musiclist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                index = (index-1)%len(musiclist)
                pygame.mixer.music.load(musiclist[index])
                pygame.mixer.music.play()
    
    text2 = font2.render(os.path.basename(musiclist[index]), True, (20,20,50))

    screen.blit(background, (-50,0))
    screen.blit(bg, (155,500))
    screen.blit(text2, (365,520))
    playbut = pygame.transform.scale(playbut, (70,70))
    pausebut = pygame.transform.scale(pausebut, (70,70))
    
    if aplay:
        screen.blit(pausebut,(370,590))
    else:
        screen.blit(playbut, (370,590))
    

    nextbut = pygame.transform.scale(nextbut, (70,70))
    screen.blit(nextbut, (460,587))
    prevbut = pygame.transform.scale(prevbut,(70,70))
    screen.blit(prevbut, (273,585))

    clock.tick(24)
    pygame.display.update()
