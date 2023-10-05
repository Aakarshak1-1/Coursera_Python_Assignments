import turtle
window=turtle.Screen()
obj=turtle.Turtle()
obj.shape("turtle")
obj.up()
for i in range(3):
    obj.forward(50)
    obj.stamp()
window.exitonclick()