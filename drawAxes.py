import turtle

# hide turtle
turtle.ht() # or turtle.hideturtle()

# set turtle speed to fastest
turtle.speed(0)

# set up the screen
turtle.setup(width=600, height=600, startx=0, starty=0) # add 50 for padding
turtle.screensize(canvwidth=500, canvheight=500)
turtle.title("Draw Axes")

def move(x, y):
	turtle.penup()
	turtle.setpos(x, y)
	turtle.pendown()

def drawAxisLine(x, y, heading=0):
	turtle.seth(heading)
	move(x, y)
	turtle.forward(500)
	turtle.left(150)
	turtle.forward(5)
	turtle.left(180)
	turtle.forward(5)
	turtle.seth(heading)
	turtle.right(150)
	turtle.forward(5)
	turtle.left(180)
	turtle.forward(5)

def drawAxisTick(text=None, heading=0):
	turtle.seth(heading)
	turtle.left(90)
	turtle.forward(3)
	turtle.left(180)
	turtle.forward(6)
	turtle.left(180)
	turtle.forward(3)
	turtle.right(90)
	if text is not None:
		turtle.penup()
		currentPos = turtle.pos()
		if heading is 0:
			turtle.setpos(currentPos[0], currentPos[1] - 15)
			turtle.write(text, align="center")
		elif heading is 90:
			turtle.setpos(currentPos[0] - 15, currentPos[1] - 5)
			turtle.write(text, align="right")
		turtle.setpos(currentPos)
		turtle.pendown()
	
def drawAxis(x, y, heading=0):
	#draw the line
	drawAxisLine(x, y, heading)
	# draw the ticks on the axis
	move(x, y)
	turtle.seth(heading)
	turtle.penup()
	turtle.forward(500/10/2)
	for i in range(9):
		turtle.pendown()
		drawAxisTick(i, heading)
		turtle.penup()
		turtle.forward(500/10)
	# last tick
	turtle.pendown()
	drawAxisTick(10, heading)

drawAxis(-250, -250)
drawAxis(-250, -250, 90)

turtle.exitonclick()