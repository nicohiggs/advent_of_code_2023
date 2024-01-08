class Node():
    def __init__(self, state, unknwowns):
        self.state = state # ".#.??"
        self.unknowns = unknowns # [3, 4]
        self.left = None
        self.right = None

def strong_check(springs, record):
    i = 0
    j = 0
    while i < len(springs):
        while springs[i] != '#':
            i += 1
        for k in range(record[j]):
            if springs[i] != '#':
                return False
            i += 1
        j += 1
        if i == len(springs) and j == len(record):
            return True
        if i != len(springs) and j == len(record):
            for char in springs[i:]:
                if char != '.':
                    return False
            return True
        if springs[i] != '.':
            return False
    return True

def check_invalid(springs, record):
    i = 0
    j = 0
    while i < len(springs):
        if springs[i] == '?':
            return True
        while i == '.':
            i += 1

def check_valid(springs, record):
    i = 0
    j = 0
    while i < len(springs):
        # get to next damage
        while springs[i] != '#':
            if springs[i] == '?':
                return True
            i += 1
            if i == len(springs):
                return False
        # check damage is valid or potentially valid
        for k in range(record[j]):
            if i == len(springs):
                return False
            if springs[i] == '.':
                return False
            i += 1
        # this spring was potentially fine, next spring
        j += 1
        # check if we reached end validly
        if i > len(springs):
            return False
        if i == len(springs):
            if j == len(record):
                return True
            return False
        if j == len(record):
            for char in springs[i:]:
                if char == '#':
                    return False
            return True
        # we finished this damage, and we aren't at end of springs or record
        # so ensure the next positon is potentially a . before continuing parsing
        if springs[i] == '#':
            return False
    return True
    


with open("input.txt") as f:
    lines = f.readlines()

result = 0
for line in lines:
    springs, record = line.strip().split(' ')
    record = [int(x) for x in record.split(',')]
    unknowns = []
    for i, char in enumerate(line):
        if char == '?':
            unknowns.append(i)
    # curr_unknowns = unknowns.copy()
    head = Node(springs, unknowns)
    curr_level = [head]
    # curr = head
    while len(unknowns) > 0:
        unknown = unknowns.pop(0)
        next_level = []
        while len(curr_level) > 0:
            curr = curr_level.pop()
            left_state = curr.state[:unknown] + '.' + curr.state[unknown+1:]
            if check_valid(left_state, record):
                curr.left = Node(left_state, unknowns)
                next_level.append(curr.left)
            right_state = curr.state[:unknown] + '#' + curr.state[unknown+1:]
            if check_valid(right_state, record):
                curr.right = Node(right_state, unknowns)
                next_level.append(curr.right)
        curr_level = next_level
    result += len(curr_level)

print(result)
    