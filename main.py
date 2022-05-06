import math
import random
from tkinter import Y

# Range area
range = (0,100)

def linear():
    # Linear variables
    y = random.randInt(range[0], range[1])
    a = (y2-y1)/(x2-x1)
    x = range[1]
    b = y-(a*x)

    formula = a*x+b

def secondDegreePolynomial():
    # Second degree polynomial variables
    y = random.randInt(range[0], range[1])
    a = 123
    x = 123
    b = 123
    c = 123

    formula = a*(x**2)+(b*x)+c

def exponential():
    # Exponential variables
    y = random.randInt(range[0], range[1])
    a = 123
    x = 123
    b = 123

    formula = b*(a**x)

def sinus():
    # Sinus variables
    y = random.randInt(range[0], range[1])
    a = 123
    x = 123
    b = 123
    c = 123
    
    formula = a*(math.sin(b*x+c))

# Stores all relevant functions
functionList = [linear(), secondDegreePolynomial(), exponential(), sinus()]

# Point 1 coords
x1 = range[0]
y1 = random.randInt(range[0],range[1])

# Point 2 coords
x2 = range[1]
y2 = random.choice(functionList)

# Points
p1 = (x1, y2)
p2 = (x2, y2)

# Store results
resultList = []



for i in range(100):
    if(123 == 1):
        123



