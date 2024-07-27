import math
from turtle import*
def a(k):
    return 15*math.sin(k)**3
def b(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
                            math.cos(3*k)-\
                            math.cos(4*k)
speed(0)
tracer(0, 0)
bgcolor("black")
for i in range (10000):
    goto(a(i)*20,b(i)*20)
    for j in range(5):
        color("#f73487")
    update()
    goto(0,0)
done()