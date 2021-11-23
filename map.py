from setting import *

text_map=[
    'WWWWWWWWWWWWWWWWWWWWWWWW',
    'W....W........WW.......W',
    'W......................W',
    'W......................W',
    'W......................W',
    'W........S.S...........W',
    'WPDDDDDDDDDDDDDDDDDDDDPW',
    'W........S.S...........W',
    'W......................W',
    'W......................W',
    'W......................W',

    'WWWWWWWWWWWWWWWWWWWWWWWW'
]
world_map=set()
light_map=set()
job_map=set()
parking_map=list()
dor_map=set()
for j,row in enumerate(text_map):
    for i,char in enumerate(row):
        if char=='W':
            world_map.add((i*TILE,j*TILE))
        if char=='S':
            light_map.add((i*TILE,j*TILE))
        if char == 'J':
            job_map.add((i * TILE, j * TILE))
        if char == 'P':
            parking_map.append((i * TILE, j * TILE))
        if char == 'D':
            dor_map.add((i * TILE, j * TILE))
