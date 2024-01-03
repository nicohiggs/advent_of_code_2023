import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

# initial grid and galaxy locations
galaxies = []
grid = np.zeros((140, 140))
for i in range(140):
    line = lines[i].strip()
    for j in range(140):
        if line[j] == '#':
            grid[i][j] = 1
            galaxies.append((i,j))

# find empties
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


# compute shortest distances
def compute_distance(p1, p2, empty_rows, empty_cols):
    distance = np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])
    distance = np.int64(distance)
    for empty_row in empty_rows:
        if (empty_row > p1[0] and empty_row < p2[0]) or (empty_row > p2[0] and empty_row < p1[0]):
            distance += 999999
    for empty_col in empty_cols:
        if (empty_col > p1[1] and empty_col < p2[1]) or (empty_col > p2[1] and empty_col < p1[1]):
            distance += 999999
    return distance
result = 0
for i in range(len(galaxies)):
    p1 = galaxies[i]
    for j in range(i+1, len(galaxies)):
        p2 = galaxies[j]
        distance = compute_distance(p1, p2, empty_rows, empty_cols)
        result += distance

print(result)