import turtle

def triangle(edge = 100):
    # Draw a triangle
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    
    # Point turtle in correct direction for next triangle
    turtle.right(60)  

for _ in range(6):
    triangle()

# Prevent window from automatically closing after triangles drawn.
# Only a problem when run from command line.
# Not necessary in IDLE.
turtle.exitonclick()
