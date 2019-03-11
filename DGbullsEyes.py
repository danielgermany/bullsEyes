from graphics import *
import random

while True:
    print("Size of window?(500 recommended)")
    try:windowSize = int(input());print("Confirmed");break
    except ValueError:print("Please enter a number")

bullEyeWin = GraphWin("Bulls Eye", windowSize,windowSize);bullEyeWin.setCoords(0,0, windowSize,windowSize)
r = random.randint(5,50)

for i in range(r):
    bullsEyeCircle = Circle(Point(windowSize/2,windowSize/2),50 * i)
    bullsEyeCircle.draw(bullEyeWin)
