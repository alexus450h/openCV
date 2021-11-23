import pygame
import pymunk
pygame.init()
WIDTH=800
HEIGHT=700

main_win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PYMUNK')
clock=pygame.time.Clock()
FPS=50
space=pymunk.Space()
space.gravity=(0,-900)
def convert_coords(point):
    return int(point[0]),int(HEIGHT-point[1])
class Ball():
    def __init__(self,x,y):
        self.body=pymunk.Body()
        self.body.position=x,y
        self.shape=pymunk.Circle(self.body,10)
        self.shape.density=1
        self.shape.elasticity=1
        space.add(self.body,self.shape)
    def draw(self):
        pygame.draw.circle(main_win,(255,0,0),convert_coords(self.body.position),10)
class String():
    def __init__(self,body1,attachment,identifier='body'):
        self.body1=body1
        if identifier=='body':
            self.body2=attachment
        elif identifier=='position':
            self.body2 = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.body2.position=attachment
        joint=pymunk.PinJoint(self.body1,self.body2)
        space.add(joint)
    def draw(self):
        pos1=convert_coords(self.body1.position)

        pos2 = convert_coords(self.body2.position)
        pygame.draw.line(main_win,(0,0,0),pos1,pos2,2)


while True:
    ball_1 = Ball(150, 350)
    ball_2 = Ball(100, 200)
    string1=String(ball_1.body,(400,650),'position')
    string2 = String(ball_1.body, ball_2.body)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    main_win.fill((255,255,255))

    ball_1.draw()
    ball_2.draw()
    string1.draw()
    string2.draw()

    pygame.display.update()
    clock.tick(FPS)
    space.step(1/FPS)