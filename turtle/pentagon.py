import turtle
window=turtle.Screen()
obj=turtle.Turtle()
angle=90
for i in range(3):
    obj.forward(50)
    obj.left(angle)
    obj.forward(50)
    obj.left(angle-45)
obj.left(-45)
window.exitonclick()