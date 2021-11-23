from tkinter import *
import random

def coords():

    for i in range(0, 20):
        z = []
        for x in range(0, 4):
            z.append(random.randint(100, 1000))
            d['line_' + str(i)] = z

    return d




pl=Tk()
d={}
coords()
print(d)
pl.geometry('640x480')
can=Canvas(pl,width=   640,height=480,bg='#eff')
for way in d.values():
   # for x in range(0,4):
    can.create_line(way[0],way[1],way[2],way[3], width=2, fill='red')
       # can.create_polygon(way[x],width=2)
   # print(way[0])
can.grid(row=0,column=0)
pl.mainloop()
