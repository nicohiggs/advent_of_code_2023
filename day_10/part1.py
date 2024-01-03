def get_next_loc(loc, pipe, prev):
    connections = []
    if pipe == '|':
        if loc[0]+1 < 140:
            connections.append((loc[0]+1, loc[1]))
        if loc[0]-1 >= 0:
            connections.append((loc[0]-1, loc[1]))
    elif pipe == '-':
        if loc[1]+1 < 140:
            connections.append((loc[0], loc[1]+1))
        if loc[1]-1 >= 0:
            connections.append((loc[0], loc[1]-1))
    elif pipe == 'L':
        if loc[0]-1 >= 0:
            connections.append((loc[0]-1, loc[1]))
        if loc[1]+1 < 140:
            connections.append((loc[0], loc[1]+1))
    elif pipe == 'J':
        if loc[0]-1 >= 0:
            connections.append((loc[0]-1, loc[1]))
        if loc[1]-1 >= 0:
            connections.append((loc[0], loc[1]-1))
    elif pipe == '7':
        if loc[0]+1 <140:
            connections.append((loc[0]+1, loc[1]))
        if loc[1]-1 >= 0:
            connections.append((loc[0], loc[1]-1))
    elif pipe == 'F':
        if loc[0]+1 < 140:
            connections.append((loc[0]+1, loc[1]))
        if loc[1]+1 < 140:
            connections.append((loc[0], loc[1]+1))
    
    if prev == connections[0]:
        return connections[1]
    return connections[0]

with open("input.txt") as f:
    lines = f.readlines()

nodes = {}
start = None
for i, line in enumerate(lines):
    for j, pipe in enumerate(line.strip()):
        if pipe == 'S':
            start = (i, j)
        if pipe != '.':
            nodes[(i, j)] = pipe

path1_loc = (start[0]+1, start[1]) # got this from looking at input, would check cardinal directions and match to pipes to generalize if needed
path1_prev = start
path1_start_found = False
path2_loc = (start[0], start[1]+1)
path2_prev = start
path_steps = 1

while path1_loc != path2_loc:
    next_loc = get_next_loc(path1_loc, nodes[path1_loc], path1_prev)
    path1_prev = path1_loc
    path1_loc = next_loc
    next_loc = get_next_loc(path2_loc, nodes[path2_loc], path2_prev)
    path2_prev = path2_loc
    path2_loc = next_loc
    path_steps += 1

print(path_steps)
        