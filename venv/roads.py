import pygame
from settings import *
class Hor_Road():
    def __init__(self,sc,x,y):
        self.serf=sc
        self.x=x
        self.y=y
        self.width=WIDTH
        self.height=HEIGHT
        self.fat=LINE_WIDTH
    def create_hor_road(self):
        pygame.draw.line(self.serf,self.x,self,self.y,self.width,self.height,self.fat)
