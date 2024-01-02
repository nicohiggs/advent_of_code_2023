import numpy as np

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

curr_nodes = []
for element in elements:
    if element[2] == 'A':
        curr_nodes.append(elements[element])
zs_hit  = [0] * len(curr_nodes)
num_steps = 0
lr_idx = 0
lr_mod = len(lr_steps)
all_zs_hit = False
while not all_zs_hit:
    next_step = lr_steps[lr_idx]

    if next_step == 'L':
        for i in range(len(curr_nodes)):
            curr_nodes[i] = elements[curr_nodes[i].left]
    else:
        for i in range(len(curr_nodes)):
            curr_nodes[i] = elements[curr_nodes[i].right]
    num_steps += 1
    lr_idx = (lr_idx + 1) % lr_mod

    for i in range(len(curr_nodes)):
        if curr_nodes[i].element[2] == 'Z':
            zs_hit[i] = num_steps

    all_zs_hit = True
    for zh in zs_hit:
        if zh == 0:
            all_zs_hit = False
            break

result = np.lcm.reduce(np.array(zs_hit, dtype=np.int64))
print(result)