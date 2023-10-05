import turtle
window=turtle.Screen()
window.bgcolor("black")

obj1=turtle.Turtle()
obj1.color("red")
obj1.shape("turtle")
distance=1
obj1.up()
obj1.speed(50)
for i in range(50):
    obj1.stamp()
    obj1.forward(distance)
    obj1.right(30)
    distance+=5
window.exitonclick()