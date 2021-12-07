import csv
import statistics
hor_pos = []
with open ('input.txt', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		for i in row:
			hor_pos.append(int(i))
			
median = statistics.median(hor_pos)
fuel_needed = 0
for i in hor_pos:
	fuel_needed += abs(i - median)
print(fuel_needed)