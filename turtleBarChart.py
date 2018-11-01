import turtle
import math

# read data
def is_float(input):
	try:
		num = float(input)
	except ValueError:
		return False
	return True

fuelConsumptions = []
with open('Fuel.txt', 'r') as fuelFile:
	lines = fuelFile.readlines()
	# Remove first line since we know it is always the same header
	del lines[0]
	for line in lines:
		if is_float(line):
			fuelConsumptions.append(float(line))

fuelConsumptions.sort()

# Get lowest and highest
lowest = fuelConsumptions[0]
highest = fuelConsumptions[-1]

# get the range
startRange = math.floor(lowest)
endRange = math.ceil(highest)

# create the segments
segments = []
segmentRange = (endRange - startRange) / 10
for i in range(10):
	segments.append(round(startRange + segmentRange * (i+1), 2))

# sort the data into the 10 segments
sortedData = {}
for segment in segments:
	sortedData[segment] = []

j = 0
for fuelConsumption in fuelConsumptions:
	if fuelConsumption > segments[j]:
		j += 1
	sortedData[segments[j]].append(fuelConsumption)

# get the highest value so that we know how many parts to divide the chart height into
maxCount = len(sortedData[max(sortedData, key=lambda k : len(sortedData[k]))])

# 10 colors
colors = ["#ff0000", "#ff0091", "#ff01dd", "#0000ff", "#049fff", "#04eaff", "#38ff01", "#fffb00", "#ffa600", "#ff6a00"]

canvas = {
	"height": 400, # min 90 for given dataset
	"width": 500, # min 370 for given dataset
}

# hide turtle
turtle.ht() # or turtle.hideturtle()

# set turtle speed to fastest
turtle.speed(0)

turtle.setup(width=canvas["width"]+120, height=canvas["height"]+120) # add 120 for padding
turtle.screensize(canvwidth=canvas["width"], canvheight=canvas["height"])
turtle.title("Fuel Consumption in 10 groups")

def move(x, y):
	turtle.penup()
	turtle.setpos(x, y)
	turtle.pendown()

def drawAxisLine(x, y, heading=0):
	turtle.seth(heading)
	move(x, y)
	turtle.forward(canvas["width"] if heading is 0 else canvas["height"])
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
	if heading is 0:
		turtle.penup()
		turtle.forward(canvas["width"]/len(sortedData)/2)

		startOfSegment = round(float(startRange), 1) # float() to make the startRange a float to render the decimal place
		for key in sortedData.keys():
			turtle.pendown()
			drawAxisTick(f"{startOfSegment} - {key}", heading)
			startOfSegment = key
			turtle.penup()
			turtle.forward(canvas["width"]/len(sortedData))

		move(-60, canvas["height"] / -2 - 30)
		turtle.write("Fuel Consumption Segments")

	elif heading is 90:
		for i in range(maxCount):
			turtle.pendown()
			drawAxisTick(i, 90)
			turtle.penup()
			turtle.forward(canvas["height"] / maxCount)
		turtle.pendown()
		drawAxisTick(i+1, 90)
    
		move(canvas["width"] / -2 - 50, 0)
		turtle.write("Count")
			
def drawBar(x, y, number, height, color):
	move(x, y)
	# draw the bar
	turtle.seth(90)
	turtle.color("#000000", color)
	turtle.begin_fill()
	turtle.forward(height)
	turtle.right(90)
	# go to middle of the top to write the value of the bar
	turtle.forward(canvas["width"]/len(sortedData)/2)
	turtle.penup()
	currentPos = turtle.pos()
	turtle.left(90)
	turtle.forward(5)
	turtle.write(number, align="center")
	turtle.setpos(currentPos)
	turtle.seth(0)
	turtle.pendown()
	turtle.forward(canvas["width"]/len(sortedData)/2)
	turtle.right(90)
	turtle.forward(height)
	turtle.right(90)
	turtle.forward(canvas["width"]/len(sortedData))
	turtle.end_fill()
	turtle.seth(0)

# draw the axes
drawAxis(canvas["width"] / -2, canvas["height"] / -2)
drawAxis(canvas["width"] / -2, canvas["height"] / -2, 90)

# draw the bars
i = 0
for key, value in sortedData.items():
	# len(value) * canvas["height"]/maxCount - scale to utilise full chart height
	drawBar(canvas["width"] / -2 + i * canvas["width"]/len(sortedData), canvas["height"] / -2, len(value), len(value) * canvas["height"]/maxCount, colors[i])
	i += 1

turtle.exitonclick()