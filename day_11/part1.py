import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

# initial grid
grid = np.zeros((140, 140))
for i in range(140):
    line = lines[i].strip()
    for j in range(140):
        if line[j] == '#':
            grid[i][j] = 1

# expanded grid
empty_rows = []
row_sum = grid.sum(axis=1)
for i in range(len(row_sum)):
    if row_sum[i] == 0:
        empty_rows.append(i)
empty_cols = []
col_sum = grid.sum(axis=0)
for i in range(len(col_sum)):
    if col_sum[i] == 0:
        empty_cols.append(i)
grid = np.insert(grid, empty_rows, 0, axis=0)
grid = np.insert(grid, empty_cols, 0, axis=1)

# get galaxy locations in new grid
galaxies = []
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i][j] == 1:
            galaxies.append((i,j))

# compute shortest distances
def compute_distance(p1, p2):
    return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])
result = 0
for i in range(len(galaxies)):
    p1 = galaxies[i]
    for j in range(i+1, len(galaxies)):
        p2 = galaxies[j]
        distance = compute_distance(p1, p2)
        result += distance

print(result)