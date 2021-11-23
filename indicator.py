import pygame

pygame.init()
menu_sc=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()
FPS=60
W,H=800,600
WHITE=(255,255,255)
RED=(255,0,0)
GRAY=(125,125,125)
BLUE=(0,0,255)
GREEN=(0,255,0)
l_x0,l_y0,dlx,dly=100,200,200,30
but_xo,but_y0,dx,dy=10,100,200,30
font=pygame.font.SysFont(None,20)
pygame.draw.rect(menu_sc,(255,255,255),(but_xo,but_y0,dx,dy))

pygame.draw.rect(menu_sc,BLUE,(l_x0,l_y0,dlx,dly))
W_X=l_x0+2
lim_x=dlx
H_Y=l_y0+dly/2
z=pygame.Rect((W_X,H_Y-5,10,10))
pows=pygame.draw.rect(menu_sc,WHITE,z)
pygame.draw.line(menu_sc,WHITE,(l_x0+2,l_y0+dly/2),(l_x0+dlx-2,l_y0+dly/2),4)
def draw_text(text,font,color,surface,x,y):
    textobj=font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

flMove=False
while 1:

    pygame.draw.rect(menu_sc, (255, 255, 255), (but_xo, but_y0, dx, dy))
    draw_text('Main menu', font, RED, menu_sc, but_xo, but_y0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if event.pos[0]>=but_xo and (but_xo+dx)>=event.pos[0] and event.pos[1]>=but_y0 and (but_y0+dy)>=event.pos[1]:

                    pygame.draw.rect(menu_sc, (255, 0, 0), (but_xo, but_y0, dx, dy))
                    draw_text('Main menu', font, GRAY, menu_sc, but_xo, but_y0)
                elif pows.collidepoint(pygame.mouse.get_pos()) :
                    z.move(pygame.mouse.get_pos())
                    flMove=True
                    # print('Hello from rect',flMove)
                # elif event.pos[0]>=but_xo and (but_xo+dx)>=event.pos[0] and event.pos[1]>=but_y0 and (but_y0+dy)>=event.pos[1]:
            # if event.type == pygame.MOUSEMOTION and flMove:
            #             # z.(pygame.mouse.get_pos())
            #     print('Ok', flMove)
            # else:
            #     flMove = False

        pygame.display.update()