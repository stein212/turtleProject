import turtle

# hide turtle
turtle.ht() # or turtle.hideturtle()

# set turtle speed to fastest
turtle.speed(0)

# set up the screen
turtle.setup(width=530, height=530, startx=0, starty=0) # add 30 for padding
turtle.screensize(canvwidth=500, canvheight=500)
turtle.title("Draw Axes")

# draw x axis
turtle.penup()
turtle.setpos(-250, -250)
turtle.pendown()

# draw the line
turtle.forward(500)

# draw the arrow
turtle.left(150)
turtle.forward(5)
turtle.left(180)
turtle.forward(5)
turtle.seth(0)
turtle.right(150)
turtle.forward(5)
turtle.left(180)
turtle.forward(5)

turtle.exitonclick()