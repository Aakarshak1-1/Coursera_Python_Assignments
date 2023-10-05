from math import dist, sqrt
import turtle 
import math
window=turtle.Screen()
obj=turtle.Turtle()
j=0
angle=30
for i in range(4):
  obj.forward(100)
  obj.left(90)
  j+=1
  if(j==4):
    obj.left(90)
    obj.forward(100)

for i in range(2):
  obj.right(angle)
  obj.forward(100)
  angle+=90
window.exitonclick()