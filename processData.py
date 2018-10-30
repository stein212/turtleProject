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

# Prepare the 10 segments
lowest = min(fuelConsumptions)
highest = max(fuelConsumptions)

print(lowest)
print(highest)

startRange = math.floor(lowest)
endRange = math.ceil(highest)

print(startRange)
print(endRange)

segments = []
segmentRange = (endRange - startRange) / 10
for i in range(10):
	segments.append(round(startRange + segmentRange * (i+1), 2))

print(segments)

# sort the data into the 10 segments
sortedData = {}
for segment in segments:
	sortedData[segment] = []

print(sortedData)

for i in fuelConsumptions:
	prevSegment = None
	for segment in segments:
		if i > segment:
			continue
		else:
			sortedData[segment].append(i)
			break
		prevSegment = segment

print(sortedData)