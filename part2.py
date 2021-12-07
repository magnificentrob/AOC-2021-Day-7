import csv
import statistics
hor_pos = []
with open ('input.txt', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		for i in row:
			hor_pos.append(int(i))

def consecsum(n):
	return n * (n+1) / 2

mean = (statistics.mean(hor_pos))
fuel_needed = 0
for i in hor_pos:
	fuel_needed += round(consecsum(abs(i - mean)))

print(fuel_needed)