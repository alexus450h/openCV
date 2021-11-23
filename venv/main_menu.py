import pygame
class Menu():
    win1=pygame.Surface((200,640))
    win1.fill((125, 125, 125))
    pygame.display.set_caption('Menu')
class Item(Menu):
    def __init__(self):
        self.options=pygame.draw.rect(win1,(0,0,0),(100,100,200,110))
    def options(self):
        pygame.draw.rect(win1,(255,255,255),(0,0,20,10))
        pygame.display.update()