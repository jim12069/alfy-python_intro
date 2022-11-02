import turtle

def rectangle():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

def big_circle(radius=30):
    turtle.circle(radius)

def little_circle(radius=20):
    turtle.circle(radius)

def ear():
    big_circle()
    little_circle()


def triangle():
    turtle.right(60)
    turtle.forward(15)
    turtle.right(120)
    turtle.forward(15)
    turtle.right(120)
    turtle.forward(15)

# Change start so that final head centered horizontally
turtle.penup()
turtle.backward(50)
turtle.pendown()

# Draw square
rectangle()

# Orient turtle and draw ear
turtle.right(90)
ear()

# Move turtle and draw other ear
turtle.penup()
turtle.forward(100)
turtle.pendown()
ear()

# Move turtle and draw right eye
turtle.right(150)
turtle.penup()
turtle.forward(30)
turtle.right(30)  # levels turtle
turtle.pendown()
turtle.circle(10)

# Turtle retrace steps back to left corner of square
turtle.right(150)
turtle.penup()
turtle.forward(30)
turtle.left(150)
turtle.forward(100)

# Draw left eye
turtle.left(150)
turtle.forward(30)
turtle.right(150)  # levels turtle
turtle.pendown()
turtle.circle(10)

# Move turtle back to left corner of square
turtle.right(30)
turtle.penup()
turtle.forward(30)

# Move turtle to center of square
turtle.left(120)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# Draw triangular nose
turtle.pendown()
triangle()

# Point turtle down and to the left
turtle.right(150)
turtle.penup()
turtle.forward(20)
turtle.right(90)
turtle.forward(25)
turtle.left(90)

# Draw semi-circle
turtle.pendown()
turtle.circle(25, extent=180)

# Hide turtle
turtle.hideturtle()

# To prevent window from closing automatically after triangles drawn
turtle.exitonclick()
