import math
import pygame
from setting import *
from map import world_map,light_map
from cros_light import Light
flag=False
def ray_casting(sc,player_pos,player_angle):
    cur_angle=player_angle-HALF_FOV
    x0,y0=player_pos

    for ray in range(NUM_RAYS):
        sin_a=math.sin(cur_angle)
        cos_a=math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x=x0+depth*cos_a
            y=y0+depth*sin_a
            if (x//TILE*TILE, y//TILE*TILE) in world_map :

                break
            pygame.draw.line(sc,DARKGRAY,player_pos,(x,y),2)
        cur_angle+=DELTA_ANGLE