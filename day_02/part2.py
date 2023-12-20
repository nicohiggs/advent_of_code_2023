with open("input.txt") as f:
    lines = f.readlines()

result = 0
for line in lines:
    if line[6] == ':':
        id = int(line[5])
        i = 8
    elif line[7] == ':':
        id = int(line[5:7])
        i = 9
    else:
        id = 100
        i = 10
    
    col_vals = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    draws = line[i:].split(';')
    for draw in draws:
        draw = draw.strip()
        ball_groups = draw.split(',')
        for ball_group in ball_groups:
            ball_group = ball_group.strip()
            num_col = ball_group.split(' ')
            num = int(num_col[0])
            col = num_col[1]
            if num > col_vals[col]:
                col_vals[col] = num
    result += (col_vals["red"] * col_vals["blue"] * col_vals["green"])
print(result)