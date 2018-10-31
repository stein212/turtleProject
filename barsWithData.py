import turtle

# hide turtle
turtle.ht() # or turtle.hideturtle()

# set turtle speed to fastest
turtle.speed(0)

sortedData = {
	6.2: [5.77, 5.9, 6.08],
	7.4: [7.16],
	8.6: [7.52, 8.15],
	9.8: [8.86, 8.99, 9.09, 9.16, 9.19, 9.36, 9.43],
	11.0: [9.84, 9.89, 10.41, 10.43, 10.59],
	12.2: [11.15, 11.38, 11.42, 11.64, 11.78, 11.93, 11.96, 12.01, 12.11, 12.12, 12.14, 12.17],
	13.4: [12.41, 12.51, 12.66, 12.87, 12.9, 12.96, 13.21, 13.23],
	14.6: [13.45, 13.66, 13.74, 14.53],
	15.8: [14.65, 14.75, 14.84, 14.86, 14.95, 15.0, 15.12, 15.17, 15.41, 15.46, 15.74, 15.76],
	17.0: [15.88, 16.12, 16.22, 16.38]
}

# 10 colors
colors = ["#ff0000", "#ff0091", "#ff01dd", "#0000ff", "#049fff", "#04eaff", "#38ff01", "#fffb00", "#ffa600", "#ff6a00"]

canvas = {
	"height": 500,
	"width": 500,
}

turtle.setup(width=canvas["width"]+100, height=canvas["height"]+100) # add 100 for padding
turtle.screensize(canvwidth=canvas["width"], canvheight=canvas["height"])
turtle.title("bars with data")

def move(x, y):
	turtle.penup()
	turtle.setpos(x, y)
	turtle.pendown()

def drawBar(x, y, height, color):
	move(x, y)
	# draw the bar
	turtle.seth(90)
	turtle.color("#000000", color)
	turtle.begin_fill()
	turtle.forward(height)
	turtle.right(90)
	turtle.forward(canvas["width"]/len(sortedData))
	turtle.right(90)
	turtle.forward(height)
	turtle.right(90)
	turtle.forward(canvas["width"]/len(sortedData))
	turtle.end_fill()
	turtle.seth(0)

# draw the bars
# counter
i = 0
for key, value in sortedData.items():
	# -250 since (0,0) is center of the chart
	# canvas["width"]/len(sortedData) - to divide the chart width equally for the bars
	# len(value) * 10 - so that it is a more visible
	# colors[i] - select the color based on the counter
	drawBar(-250 + i * canvas["width"]/len(sortedData), -250, len(value) * 10, colors[i])
	i += 1

# scale bars to utilise full canvas height
turtle.clear()

# get the highest value so that we know how many parts to divide the chart height into
maxCount = len(sortedData[max(sortedData, key=lambda k : len(sortedData[k]))])

i = 0
for key, value in sortedData.items():
	# len(value) * canvas["height"]/maxCount - scale to utilise full chart height
	drawBar(-250 + i * canvas["width"]/len(sortedData), -250, len(value) * canvas["height"]/maxCount, colors[i])
	i += 1

turtle.exitonclick()