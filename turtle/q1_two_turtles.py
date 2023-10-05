import turtle
window=turtle.Screen()
window.bgcolor("black")
obj1=turtle.Turtle()
obj1.color("red")
obj1.pensize(5)
obj2=turtle.Turtle()
obj2.color("blue")
obj2.pensize(5)

obj1.left(180)
obj1.forward(100)

obj2.right(90)
obj2.forward(100)
obj2.right(-90)
obj2.forward(100)
window.exitonclick()