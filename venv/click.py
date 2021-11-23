from tkinter import *
def flop(evemt):
    global inst
    inst=inst + 1
    l['text']=str(inst)
root=Tk()
global inst
inst=0
l=Label(root,text=str(inst),fg='red',font=('Arial,24'))
l.pack()
root.geometry('500x400')
root.bind('<Button-1>',flop)
root.mainloop()
