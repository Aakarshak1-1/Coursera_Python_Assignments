import turtle
window=turtle.Screen()
window.bgcolor("black")
object=turtle.Turtle()
object.color("red")
for i in range(4):
   object.forward(150)
   object.left(90)
window.exitonclick()