import math
import random

# Range area
range = (0,100)

def linear(x1,y1,x2,y2):
    # Linear variables
    #y = random.randint(range[0], range[1])
    x = range[1]
    a = (y2-y1)/(x2-x1)
    b = y2-(a*x)

    formula = a*x+b
    return formula

def secondDegreePolynomial():
    # Second degree polynomial variables
    y = random.randint(range[0], range[1])
    x = range[1]
    a = 123
    b = 123
    c = 123

    formula = a*(x**2)+(b*x)+c

def exponential(x1,y1,x2,y2):
    # Exponential variables
    #y = random.randint(range[0], range[1])
    a = (y2/y1)**(1/(x2-x1))
    x = range[1]
    b = y2/(a**x)

    formula = b*(a**x)
    return formula

def sinus():
    # Sinus variables
    y = random.randint(range[0], range[1])
    a = 123
    x = 123
    b = 123
    c = 123
    
    formula = a*(math.sin(b*x+c))


# secondDegreePolynomial(),
# , sinus()

# Point 1 coords
x1 = range[0]
y1 = random.randint(range[0],range[1])

# Point 2 coords
x2 = range[1]
y2 = random.randint(range[0],range[1])

# Stores all relevant functions
functionList = [linear(x1,y1,x2,y2), exponential(x1,y1,x2,y2)]

# Points
p1 = (x1, y2)
p2 = (x2, y2)

# Store results
resultList = []

for i in range(100):
    if(1 == 1):
        resultList.append(random.choice(functionList))
print(resultList)