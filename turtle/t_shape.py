import turtle
window=turtle.Screen()
window.bgcolor("black")
object=turtle.Turtle()
object.color("red")
object.pensize(10)
for i in range(2):
    object.left(90)
    object.forward(150)
object.right(180)
object.forward(300)
window.exitonclick()