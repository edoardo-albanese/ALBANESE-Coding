from turtle import *

t = Turtle()
#cb = t.screensize()
#print(cb) non funziona

def polygon(sides : int, length : int, pos : tuple):
    t.pu()
    t.goto(pos)
    t.pd()
    
    for i in range(sides):
        t.forward(length)
        t.right(360/sides)
    t.pu()

polygon(6, 60, (70,40))
polygon(12, 40, (-200,-50))
polygon(4, 50, (220, -70))
polygon(8, 40, (-200, 260))

wait = input("press enter...")