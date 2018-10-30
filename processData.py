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

print(fuelConsumptions)
print()

# Prepare the 10 segments
lowest = fuelConsumptions[0]
highest = fuelConsumptions[-1]

print(lowest)
print(highest)
print()

startRange = math.floor(lowest)
endRange = math.ceil(highest)

print(startRange)
print(endRange)
print()

segments = []
segmentRange = (endRange - startRange) / 10
for i in range(10):
	segments.append(round(startRange + segmentRange * (i+1), 2))

print(segments)
print()

# sort the data into the 10 segments
sortedData = {}
for segment in segments:
	sortedData[segment] = []

print(sortedData)
print()

j = 0
for fuelConsumption in fuelConsumptions:
	if fuelConsumption > segments[j]:
		j += 1
	sortedData[segments[j]].append(fuelConsumption)

print(sortedData)
print()