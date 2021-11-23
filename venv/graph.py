from graphics import *
from tkinter import *
import time
my_win=GraphWin('Town',width=800,height=800)
b=Button(my_win,text='Ok')
my_text=Text(Point(400,400),'Kolomiysa')
my_text.setTextColor('red')
my_text.draw(my_win)
obj = Circle(Point(200, 200), 50)
obj.setFill('red')
obj.draw(my_win)
time.sleep(0.5)
obj.undraw()

obj.move(45,56)
obj.draw(my_win)
time.sleep(0.5)
my_win.close()