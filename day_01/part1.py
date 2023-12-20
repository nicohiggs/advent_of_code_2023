with open("input.txt") as f:
	lines = f.readlines()

result = 0
for line in lines:
	numbers = []
	for char in line:
		if char.isnumeric():
			numbers.append(char)
	cal_val = int(numbers[0] + numbers[-1])
	result += cal_val
print(result)
	