import turtle

t = turtle.Turtle()

def polygon(sides : int, length : int, pos : tuple):
    t.pu()
    t.goto(pos)
    t.pd()
    
    for i in range(sides):
        t.forward(length)
        t.right(360/sides)
    t.pu()

polygon(5, 60, (70,40))
polygon()

wait = input("press enter...")