from random import randint
from turtle import *

speed('fastest')
pensize(2)

def move(x, y):
    penup()
    goto(x,y)
    pendown()

def prostokat(x, y, dlugibok, krotkibok):
    move(x,y)
    rt(-90)
    fd(krotkibok)
    rt(-90)
    fd(dlugibok)
    rt(-90)
    fd(krotkibok)
    rt(-90)
    fd(dlugibok)

def obrazek(n): #n to ilość prostokątów
    bokA = 15 
    bokB = 15
    next=0
    for i in range(n):
        bokB = bokB + randint(3,10)
        prostokat(-350+next,-200,bokA,bokB)
        next = next + bokA + 5

obrazek(50)
input()
