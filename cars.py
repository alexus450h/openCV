from setting import *
import pygame
import math
from map import dor_map
class Cars:
    def __init__(self):
        self.x,self.y=player_pos
        self.angle=player_ang
        self.x1,self.y1=mo
    @property
    def pos(self):
        return self.x,self.y
    def movement(self):
        keys=pygame.key.get_pressed()
        sin_a=math.sin(self.angle)
        cos_a = math.cos(self.angle)
        print(len(dor_map))

        if keys[pygame.K_w]:
            self.x+=player_speed*cos_a
            self.y+=player_speed*sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle-=0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
        def riding(s)