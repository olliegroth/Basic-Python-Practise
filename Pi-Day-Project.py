import turtle

window=turtle.Screen()
window.bgcolor("black")
window.title("Pi Day Turtle Art")

turtle.pencolor("red")
turtle.speed(0)

for i in range(0,60):
    turtle.forward(1)
    turtle.left(1.5)
    
turtle.forward(100)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(100)

for i in range(0,90):
    turtle.forward(1)
    turtle.left(1.5)
for i in range(0,5):
    turtle.forward(3)
    turtle.left(1)
for i in range(0,5):
    turtle.forward(1)
    turtle.left(5)

for i in range(0,14):
    turtle.forward(0.5)
    turtle.left(10)
    
for i in range(0,3):
    turtle.forward(10)
    turtle.right(10)

for i in range(0,10):
    turtle.right(10)
    turtle.forward(4)
    
turtle.left(4.7)
turtle.forward(95)
turtle.right(90)
turtle.forward(40)

for i in range(0,2):
    turtle.left(90)
    turtle.forward(30)
turtle.left(0.4)
turtle.forward(120)

for i in range(0,100):
    turtle.forward(1)
    turtle.left(1)

turtle.left(140)

for i in range(0,17):
    turtle.right(3)
    turtle.forward(4)

turtle.right(99.5)
turtle.forward(90)

for i in range(0,30):
    turtle.right(2)
    turtle.forward(1)

for i in range(0,30):
    turtle.left(5)
    turtle.forward(1)

turtle.speed(1)
turtle.penup()
turtle.forward(70)
