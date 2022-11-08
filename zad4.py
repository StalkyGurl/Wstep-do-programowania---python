from random import randint
from turtle import *

speed('fastest')
pensize(2)

def move(x, y):
    penup()
    goto(x,y)
    pendown()

def rectangle(x, y, longside, shortside):
    move(x,y)
    rt(-90)
    fd(shortside)
    rt(-90)
    fd(longside)
    rt(-90)
    fd(shortside)
    rt(-90)
    fd(longside)

def image(n): #n to ilość prostokątów
    sideA = 15 
    sideB = 15
    next=0
    for i in range(n):
        sideB = sideB + randint(3,10)
        rectangle(-350+next,-200,sideA,sideB)
        next = next + sideA + 5

image(50)
input()
