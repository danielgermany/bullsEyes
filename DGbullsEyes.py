from graphics import *
import random

while True:
    print("Size of window?(500 recommended)")
    try:windowSize = int(input());print("Confirmed");break
    except ValueError:print("Please enter a number")

bullEyeWin = GraphWin("Bulls Eye", windowSize,windowSize);bullEyeWin.setCoords(0,0, windowSize,windowSize)

def bulleye(r,colorR,colorG,colorB):
    for i in range(r):
        bullsEyeCircle = Circle(Point(windowSize/2,windowSize/2),((windowSize/4)/r) * (r-i))
        
        if i % 2 == 0:bullsEyeCircle.setFill(color_rgb(colorR,colorG,colorB))
        else:bullsEyeCircle.setFill(color_rgb(0,0,0))
        
        bullsEyeCircle.draw(bullEyeWin)

bulleye(random.randint(5,15),random.randint(0,255),random.randint(0,255),random.randint(0,255))
