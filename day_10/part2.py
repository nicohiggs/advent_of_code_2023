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
on_loop = []
in_out = []
for i, line in enumerate(lines):
    on_loop.append([False]*140)
    in_out.append(['O']*140)
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

on_loop[start[0]][start[1]] = True
on_loop[path1_loc[0]][path1_loc[1]] = True
on_loop[path2_loc[0]][path2_loc[1]] = True

points = [start]

while path1_loc != path2_loc:
    next_loc = get_next_loc(path1_loc, nodes[path1_loc], path1_prev)
    path1_prev = path1_loc
    path1_loc = next_loc
    next_loc = get_next_loc(path2_loc, nodes[path2_loc], path2_prev)
    path2_prev = path2_loc
    path2_loc = next_loc

    on_loop[path1_loc[0]][path1_loc[1]] = True
    on_loop[path2_loc[0]][path2_loc[1]] = True


result = 0
for i in range(140):
    for j in range(140):
        if on_loop[i][j]:
            in_out[i][j] = nodes[(i, j)]
            continue
        # row to right
        count = 0
        for k in range(j+1, 140):
            if on_loop[i][k]:
                # counting for parity of 'lines crossed in this direction'
                if nodes[(i, k)] in '|JL': # since F---J and L-7 are essentially vertical bars we can count J and L individually for parity
                    count += 1
        if count % 2 != 0:
            in_out[i][j] = 'I'
            result += 1

for row in in_out:
    print(''.join(row))
print(result)