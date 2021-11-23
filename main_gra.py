import pygame
from  setting import *
from cars import Cars
import math
from map import world_map,light_map,job_map,parking_map,dor_map
from ray_casting import *
from cros_light import *
pygame.init()
sc=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
car=Cars()
light=Light()
color=light.stan

mow_pos=parking_map[0]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    car.movement()
    sc.fill(BLACK)
    ray_casting(sc,car.pos,car.angle)
    # pygame.draw.circle(sc, RED, (player_pos[0] + TILE / 2, player_pos[1] + +TILE / 2), 12)
    pygame.draw.circle(sc,GREEN,(int(car.x),int(car.y)),12)
    pygame.draw.line(sc,GREEN,car.pos,(car.x+WIDTH*math.cos(car.angle),car.y+WIDTH*math.sin(car.angle)))
    for x,y in world_map:
        pygame.draw.rect(sc,WHITE,(x,y,TILE,TILE),2)
    for x, y in dor_map:
        pygame.draw.rect(sc, DARKGRAY, (x, y, DOR_TILE, DOR_TILE))
    for x,y in light_map:

        pygame.draw.circle(sc,color,(x+RADIUS,y+RADIUS),RADIUS)
        pygame.draw.circle(sc, RED, (x , y), RADIUS)
    for x,y in job_map:
        pygame.draw.rect(sc,RED,(x,y,TILE,TILE))
    for x, y in parking_map:
        pygame.draw.rect(sc, GREEN, (x, y, TILE, TILE))
    pygame.draw.circle(sc, RED, (mow_pos[0] + TILE / 2, mow_pos[1] + +TILE / 2), 12)
    pygame.display.update()
    clock.tick(FPS)