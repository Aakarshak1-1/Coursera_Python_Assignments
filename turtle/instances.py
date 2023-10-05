import turtle
window=turtle.Screen()
window.bgcolor("black")
obj1=turtle.Turtle()
obj1.color("red")
obj1.pensize(5)
obj2=turtle.Turtle()
obj2.color("green")
obj2.pensize(5)
for i in range(3):
    obj1.forward(100)
    obj1.left(120)
for i in range(4):
    obj2.forward(100)
    obj2.left(90)
window.exitonclick()