class Node:
    def __init__(self, element, left, right):
        self.element = element
        self.left = left
        self.right = right

with open("input.txt") as f:
    lines = f.readlines()

lr_steps = lines[0].strip()
elements = {}
for line in lines[2:]:
    line = line.strip()
    split_line = line.split(' ')
    element = split_line[0]
    left = split_line[2][1:-1]
    right = split_line[3][:-1]
    elements[element] = Node(element, left, right)

curr_node = elements["AAA"]
num_steps = 0
lr_idx = 0
lr_mod = len(lr_steps)
while curr_node.element != "ZZZ":
    next_step = lr_steps[lr_idx]
    if next_step == 'L':
        curr_node = elements[curr_node.left]
    else:
        curr_node = elements[curr_node.right]
    num_steps += 1
    lr_idx = (lr_idx + 1) % lr_mod
    
print(num_steps)