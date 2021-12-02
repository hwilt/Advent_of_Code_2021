f = open("TXT.txt")

depth_measurements = []
for line in f:
	depth_measurements.append(int(line.strip()))
i = 0
f.close()

# Day 1 Part 1:
measurement_increases = 0
while i < len(depth_measurements) - 1:
	if depth_measurements[i+1] - depth_measurements[i] > 0:
		measurement_increases += 1
	i += 1
print("Number of measurement increases: " + str(measurement_increases))

# Day 1 Part 2:
depth_clusters = 0
i = 0
while i < len(depth_measurements) - 3:
	cluster_one = depth_measurements[i] + depth_measurements[i+1] + depth_measurements[i+2]
	cluster_two = depth_measurements[i+1] + depth_measurements[i+2] + depth_measurements[i+3]
	#print("A:", cluster_one, "B:", cluster_two)
	if cluster_two - cluster_one > 0:
		depth_clusters += 1
		#print("increase")
	i += 1
print("Number of cluster increases: " + str(depth_clusters))

