import math

WIDTH=1200
HEIGHT=600
HALF_WIDTH=WIDTH//2
HALF_HEIGHT=HEIGHT//2
# colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(220,0,0)
GREEN=(0,220,0)
BLUE=(0,0,220)
DARKGRAY=(110,110,110)
PURPLE=(120,0,120)
YELLOW=(255,255,0)
BROWN=(165,42.42)
FPS=60
#player
player_pos=(HALF_WIDTH,HALF_HEIGHT)
player_ang=0
player_speed=2

#look
FOV=math.pi/3
HALF_FOV=FOV/2
NUM_RAYS=6
MAX_DEPTH=800
DELTA_ANGLE=FOV/NUM_RAYS
TILE=50
DOR_TILE=50
#lights
RADIUS=TILE/5