with open("input.txt") as f:
    lines = f.readlines()

class Number:
    def __init__(self, value, positions) -> None:
        self.value = value
        self.positions = positions
        self.is_part_num = False

class Symbol:
    def __init__(self, position, symbol) -> None:
        self.position = position
        self.symbol = symbol
        self.gear_ratio = 0

numbers = []
pos2number = {}
symbols = []
for line_num, line in enumerate(lines):
    line = line.strip()
    i = 0
    while i < len(line):
        if line[i].isnumeric():
            curr_num = int(line[i])
            curr_positions = [(line_num, i)]
            while i+1 < len(line) and line[i+1].isnumeric():
                i += 1
                curr_num = curr_num * 10
                curr_num += int(line[i])
                curr_positions.append((line_num, i))
            new_number = Number(curr_num, curr_positions)
            numbers.append(new_number)
            for position in new_number.positions:
                pos2number[position] = new_number
        elif line[i] != '.':
            symbols.append(Symbol((line_num, i), line[i]))
        i += 1

max_pos = 139
for symbol in symbols:
    curr_pos = symbol.position
    possible_num_positions = [
        (curr_pos[0] - 1, curr_pos[1] - 1),
        (curr_pos[0] - 1, curr_pos[1]),
        (curr_pos[0] - 1, curr_pos[1] + 1),
        (curr_pos[0], curr_pos[1] - 1),
        (curr_pos[0], curr_pos[1] + 1),
        (curr_pos[0] + 1, curr_pos[1] - 1),
        (curr_pos[0] + 1, curr_pos[1]),
        (curr_pos[0] + 1, curr_pos[1] + 1)
    ]
    adjacent_numbers = []
    for possible_position in possible_num_positions:
        if possible_position[0] >= 0 and possible_position[0] <= max_pos and possible_position[1] >= 0 and possible_position[1] <= max_pos:
            if possible_position in pos2number:
                if pos2number[possible_position] not in adjacent_numbers:
                    adjacent_numbers.append(pos2number[possible_position])
    if len(adjacent_numbers) == 2:
        symbol.gear_ratio = adjacent_numbers[0].value * adjacent_numbers[1].value


result = 0
for symbol in symbols:
    result += symbol.gear_ratio

print(result)