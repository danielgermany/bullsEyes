from graphics import *
import random

while True:
    print("Size of window?(500 recommended)")
    try:windowSize = int(input());print("Confirmed");break
    except ValueError:print("Please enter a number")
    
while True:
    print("How many rings should be in the bulls eye?")
    try:rings = int(input());print("Confirmed");break
    except ValueError:print("Please enter a number")
    
while True:
    print("""Type of Bulls Eye?
1. Original
2. Original (Diffrent Color)
3. Gradient
(Enter number corresponding to your answer)""")
    try:
        userAnswer = int(input())
        if 1 <= userAnswer <= 3:print("Confirmed");break
        else:print("Enter a number inside the bounds of 1 - 3")
    except ValueError:print("Please enter a number")
    
while True:
    print("How many Bulls Eyes'?")
    try:bullCount = int(input());print("Confirmed");break
    except ValueError:print("Please enter a number")
                        
bullEyeWin = GraphWin("Bulls Eye", windowSize,windowSize);bullEyeWin.setCoords(0,0, windowSize,windowSize)

def bulleye(r,colorR,colorG,colorB,bullType,x,y):
    if bullType == 1:
        for i in range(r):
            bullsEyeCircle = Circle(Point(x,y),((windowSize/8)/r) * (r-i))
            
            if i % 2 == 0:bullsEyeCircle.setFill(color_rgb(255,0,0))
            else:bullsEyeCircle.setFill(color_rgb(0,0,0))
            
            bullsEyeCircle.draw(bullEyeWin)
    elif bullType == 2:        
        for i in range(r):
            bullsEyeCircle = Circle(Point(x,y),((windowSize/8)/r) * (r-i))
            
            if i % 2 == 0:bullsEyeCircle.setFill(color_rgb(colorR,colorG,colorB))
            else:bullsEyeCircle.setFill(color_rgb(0,0,0))
            
            bullsEyeCircle.draw(bullEyeWin)
    elif bullType == 3:
        for i in range(r):
            bullsEyeCircle = Circle(Point(x,y),((windowSize/8)/r) * (r-i))

            incR = int(colorR/r)
            incG = int(colorG/r)
            incB = int(colorB/r)
            
            bullsEyeCircle.setFill(color_rgb(colorR - (incR * i),colorG - (incG *i),colorB - (incB * i)))
            bullsEyeCircle.draw(bullEyeWin)



if bullCount == 1:
    bulleye(rings,random.randint(0,255),random.randint(0,255),random.randint(0,255),userAnswer,windowSize/2,windowSize/2)
else:
    for i in range(bullCount):
        pos1 = random.randint(0,windowSize)
        pos2 = random.randint(0,windowSize)
        bulleye(rings,random.randint(0,255),random.randint(0,255),random.randint(0,255),userAnswer,pos1,pos2)
