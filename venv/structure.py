import random
from tkinter import *
import time
def  det(x1,y2,x2,y1):
    det_v=x1*y2-x2*y1
    return det_v
def ser_per(x1,y2,y1,x2,x3,y4,x4,y3):
    px=(det(x1,y2,x2,y1)*det(x3,1,x4,1)-det(x3,y4,x4,y3)*det(x1,1,x2,1))/(det(x1,1,x2,1)*det(y3,1,y4,1)-det(y1,1,y2,1)*det(x3,1,x4,1))
    py = det(x1, y2, x2, y1) * det(y3, 1, y4, 1) - det(x3, y4, x4, y3) * det(y1, 1, y2, 1)/(det(x1,1,x2,1)*det(y3,1,y4,1)-det(y1,1,y2,1)*det(x3,1,x4,1))
    return px,py
def coords():
    d={}

    for i in range(0,4):
        z = []
        for x in range(0,4):
            z.append(random.randint(0, 1000))
            d['line_'+str(i)]=z

    print(d)
def moveRun():

        c.move(ball1, 0, -12)
def moveStop():

        c.move(ball1, 0, 12)
x1=0;y1=0;x2=800;y2=670;x3=0;y3=650;x4=800;y4=0;
dp=2
r=Tk()

r.geometry('800x650+100+10')
b1=Button(r,text='Start', command=moveRun).grid(row=0,column=10)
b2=Button(r,text='Stop', command=moveStop).grid(row=1,column=10)
c=Canvas(r,width=800,height=650,bg='#addfae')
c.focus_set()
c.grid(row=0,column=0)
c.create_line([x1,y1],[x2,y2],width=3,fill='gray')
c.create_line([x3,y3],[x4,y4],width=3,fill='red')
x,y=ser_per(x1,y2,y1,x2,x3,y4,x4,y3)
ball=c.create_oval(x-dp,y-dp,x+dp,y+dp,fill='blue')
ball1=c.create_oval(x-dp,y-dp,x+dp,y+dp,fill='green')

# time.sleep(1)
r.mainloop()