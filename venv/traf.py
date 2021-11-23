import pygame
import random
import pygame_widgets
from settings import *
from pygame_widgets.slider import Slider
from pygame_widgets.toggle import Toggle
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
pygame.init()


def menu():
    global sl_first
    menu1=pygame.Surface((600,640))
    menu1.fill(COLORS['gray'])

    x,y=1,120
    width=198
    height=10
    sl_first=Slider(win,x,y,width,height,min=0, max=99, step=1,colour=COLORS['gray'])
    return sl_first

    # win.blit(menu1, (600, 0))





win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_icon(pygame.image.load('d:/samles/st.png'))
timer=pygame.time.Clock()
running=True
flLeft=flRight=False
speed=5
dist=30
wid=10
x1=0
y1=HOR_Y
y2=HOR_Y+LINE_WIDTH
x2=WIDTH


signal=False


X_rstop=WIDTH-X+LINE_WIDTH+18
X_lstop=X-LINE_WIDTH-3
while running:
    events = pygame.event.get()
    # menu()
    for event in events:
        if event.type == pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                flLeft=True
            elif event.key==pygame.K_RIGHT:
                flRight = True
        elif  event.type==pygame.KEYUP:
            if event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
                flLeft = flRight = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==3:

                print('menu')
            elif event.button==1:
                sl_first.moveX(6)
                print('ok')

    if flLeft:
            X-=speed
    elif flRight:
            X+=speed
    win.fill(COLORS['white'])
    r_left=pygame.draw.line(win, COLORS['gray'], (0, HOR_Y - INTER), (WIDTH, HOR_Y - INTER), LINE_WIDTH)
    l1=pygame.draw.line(win, COLORS['white'], (0, HOR_Y - INTER + LINE_WIDTH // 2),
                     (WIDTH, HOR_Y- INTER + LINE_WIDTH // 2), 1)
    r_right=pygame.draw.line(win, COLORS['gray'], (0, HOR_Y - INTER + LINE_WIDTH), (WIDTH, HOR_Y - INTER + LINE_WIDTH),
                     LINE_WIDTH)


    pygame.draw.line(win, COLORS['gray'], (0, HOR_Y+INTER), (WIDTH, HOR_Y+INTER), LINE_WIDTH)
    pygame.draw.line(win, COLORS['white'], (0, HOR_Y+INTER + LINE_WIDTH // 2), (WIDTH, HOR_Y+INTER + LINE_WIDTH // 2), 1)
    pygame.draw.line(win, COLORS['gray'], (0, HOR_Y+INTER + LINE_WIDTH), (WIDTH, HOR_Y+INTER + LINE_WIDTH), LINE_WIDTH)

    pygame.draw.line(win, COLORS['gray'], (0, HOR_Y), (WIDTH, HOR_Y), LINE_WIDTH)
    pygame.draw.line(win, COLORS['white'], (0, HOR_Y+LINE_WIDTH//2), (WIDTH, HOR_Y+LINE_WIDTH//2), 1)
    pygame.draw.line(win, COLORS['gray'], (0, HOR_Y+LINE_WIDTH), (WIDTH, HOR_Y+LINE_WIDTH), LINE_WIDTH)
   #vertical
    pygame.draw.line(win, COLORS['gray'], (X, 0), (X, HEIGHT), 12)
    pygame.draw.line(win, COLORS['white'], (X+LINE_WIDTH//2, 0), (X+LINE_WIDTH//2, HEIGHT), 1)
    pygame.draw.line(win, COLORS['gray'], (X+LINE_WIDTH, 0), (X+LINE_WIDTH, HEIGHT), 12)
    # pygame.draw.line(win, COLORS['white'], (0, 406), (640, 406), 1)
        # pygame.display.update()

    if x1==X_lstop and signal==True:

        x1=X_lstop
    elif x1==X and signal==False:
        y2 += speed
    else:
        x1 += speed
    if x2 == X_rstop and signal == True:

        x2=X_rstop
    else:

        x2 -= speed
    pygame.draw.circle(win, (255, 255, 255), (x1, y2), 5)

    pygame.draw.circle(win, (255, 255, 255), (x2, y1), 5)

    pygame_widgets.update(events)
    pygame.display.update()
    timer.tick(60)
