import pygame
import pymunk
pygame.init()
WIDTH=800
HEIGHT=700
BALL_RADIUS=20
main_win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PYMUNK')
clock=pygame.time.Clock()
FPS=60
space=pymunk.Space()
image=pygame.image.load('d:/img/ball1.jpg')
image=pygame.transform.scale(image,(BALL_RADIUS*2,BALL_RADIUS*2))
class Ball():
    def __init__(self,x=100):
        self.body = pymunk.Body()
        self.body.position = 400, 600
        self.shape = pymunk.Circle(self.body, BALL_RADIUS)
        space.add(self.body, self.shape)
        self.shape.density = 3
        self.shape.elasticity = 1
        space.gravity = 0, -1000
    def draw(self):
        x, y = convert_coords(self.body.position)
        main_win.blit(image,(int(x)-BALL_RADIUS,int(y)-BALL_RADIUS))
        # pygame.draw.circle(main_win, (255, 0, 0), (int(x), int(y)), BALL_RADIUS)

class Floor():
    def __init__(self):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, (0, 30), (800, 30), 5)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.line(main_win, (0, 0, 0), (0, 670), (800, 670), 15)
        # main_win.blit(image, (int(x) - BALL_RADIUS, int(y) - BALL_RADIUS))

def convert_coords(point):
    return point[0],HEIGHT-point[1]
ball=Ball()
ball2=Ball(100)
ball3=Ball(200)
# ball33=Ball(200)
flor=Floor()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    main_win.fill((255,255,255))

    ball.draw()
    ball2.draw()
    ball3.draw()
    # ball33.draw()
    flor.draw()
    clock.tick(FPS)

    pygame.display.update()
    space.step(1/FPS)