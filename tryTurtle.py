import turtle

# hide turtle
turtle.ht() # or turtle.hideturtle()

# set turtle speed to fastest
turtle.speed(0)
# fastest: 0
# fast: 10
# normal: 6
# slow: 3
# slowest: 1


# draw square manually
for i in range(4):
	turtle.forward(10)
	turtle.left(90)

# move turtle position
turtle.penup()
turtle.setpos(30, 0)
turtle.pendown()

# draw circle using turtle's api
turtle.circle(10) # the circle draws from the bottom -> top -> bottom

# move turtle position
turtle.penup()
turtle.setpos(60, 0)
turtle.pendown()

# draw an arc
turtle.circle(10, 90)

# move turtle position
turtle.penup()
turtle.setpos(90, 0)
turtle.pendown()

# draw a diamond
turtle.setheading(0) # set the direction the turtle is facing
turtle.circle(10, steps = 4)

# move turtle position
turtle.penup()
turtle.setpos(120, 0)
turtle.pendown()

# draw a square
turtle.left(45)
turtle.circle(10, steps = 4)

# move turtle position
turtle.penup()
turtle.setpos(0, 30)
turtle.pendown()

# draw a blue line
turtle.color("blue")
turtle.forward(10)

# set color back to black
turtle.color("black")

# move turtle position
turtle.penup()
turtle.setpos(30, 30)
turtle.pendown()

# draw rectangle with green fill and black stroke
turtle.setheading(0)
turtle.color("black", "green")
turtle.begin_fill()
turtle.forward(10)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.end_fill()

# move turtle position
turtle.penup()
turtle.setpos(60, 30)
turtle.pendown()

# write some text
turtle.write("Hello World!", font=("Arial", 8, "normal"))

# move turtle position
turtle.penup()
turtle.setpos(120, 30)
turtle.pendown()

# write some text
turtle.write("Hello World Again!", font=("Arial", 10, "bold"))
# turtle.write has 2 more parameters which is align and move, align is more important in this project

turtle.exitonclick()