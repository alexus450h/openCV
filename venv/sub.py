import pygame
pygame.init()
sur=pygame.display.set_mode((640,400))
w,h=640,0
pygame.display.set_caption(("Fonts"))
pygame.display.set_icon(pygame.image.load('d:/samles/st.png'))
clock=pygame.time.Clock()
FPS=30
WHITE=(255,255,255)
RED=(255,0,0)
f=pygame.font.get_fonts()


while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    for x in f:
        f_sys = pygame.font.SysFont(x, 24)
        text = f_sys.render("Hello", 1, RED)
        pos = text.get_rect(center=(w // 2, h // 2))
        h += 0.1
        sur.fill(WHITE)
        sur.blit(text, pos)
        pygame.display.update()
    clock.tick(FPS)