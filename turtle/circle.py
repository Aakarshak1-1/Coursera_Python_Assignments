import turtle
window = turtle.Screen()
obj = turtle.Turtle()
obj.shape("turtle")
obj.up()
for i in range(10):
    obj.forward(50)
    obj.stamp()
    obj.forward(-50)
    obj.right(36)
window.exitonclick()
