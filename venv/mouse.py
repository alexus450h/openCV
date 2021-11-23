import pygame

pygame.init()
sc=pygame.display.set_mode((800,600))
pygame.display.set_caption('Hello mouse')
clock=pygame.time.Clock()
FPS=60
W,H=800,600
WHITE=(255,255,255)
RED=(255,0,0)
GRAY=(125,125,125)
sp=ep=None
flDraw=False
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and  event.button==1:
            flDraw=True
            sp=event.pos
        elif event.type==pygame.MOUSEMOTION:
            if flDraw:
                pos=event.pos
                width=pos[0]-sp[0]
                height=pos[1]-sp[1]
                pygame.draw.rect(sc,RED,(sp[0],sp[1],width,height))
                pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            flDraw=False

    clock.tick(FPS)