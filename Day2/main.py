f = open("TXT.txt")

data = []
for line in f:
	data.append(line.strip().split(" "))
	
# Day 2 Part 1
horizontal = 0
depth = 0
i = 0
while i < len(data):
	if data[i][0] == 'forward':
		horizontal += int(data[i][1])
	elif data[i][0] == 'down':
		depth += int(data[i][1])
	else:
		depth -= int(data[i][1])
	i += 1
multi = horizontal * depth
print(multi)

# Day 2 Part 2
horizontal = 0
depth = 0
aim = 0
i = 0
while i < len(data):
	if data[i][0] == 'forward':
		horizontal += int(data[i][1])
		depth += aim * int(data[i][1])
	elif data[i][0] == 'down':
		aim += int(data[i][1])
	else:
		aim -= int(data[i][1])
	i += 1
multi = horizontal * depth
print(multi)


f.close()
