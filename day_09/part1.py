with open("input.txt") as f:
    lines = f.readlines()
result = 0
for line in lines:
    ts = line.strip().split(' ')
    ts = [int(x) for x in ts]
    
    diffs = []
    curr_diff = ts
    all0 = False
    while not all0:
        new_diff = []
        all0 = True
        for i in range(1, len(curr_diff)):
            new_val = curr_diff[i] - curr_diff[i-1]
            if new_val != 0:
                all0 = False
            new_diff.append(new_val)
        if not all0:
            diffs.append(new_diff)
        curr_diff = new_diff

    new_val = 0
    for diff in diffs[::-1]:
        new_val += diff[-1]
    new_val += ts[-1]
    result += new_val

print(result)
        