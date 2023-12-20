with open("input.txt") as f:
	lines = f.readlines()

word2num = {
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": '9'
}

result = 0
for line in lines:
	numbers = []
	i = 0
	while i < len(line):
		if line[i].isnumeric():
			numbers.append(line[i])
		elif line[i] in ['o', 't', 'f', 's', 'e', 'n']:
			if i <= len(line) - 3:
				if line[i:i+3] in word2num:
					numbers.append(word2num[line[i:i+3]])
			if i <= len(line) - 4:
				if line[i:i+4] in word2num:
					numbers.append(word2num[line[i:i+4]])
			if i <= len(line) - 5:
				if line[i:i+5] in word2num:
					numbers.append(word2num[line[i:i+5]])
		i += 1
	cal_val = int(numbers[0] + numbers[-1])
	result += cal_val
print(result)