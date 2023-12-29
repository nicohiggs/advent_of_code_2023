with open("input.txt") as f:
    lines = f.readlines()

split_line = lines[0].split(' ')
times = [int(x.strip()) for x in split_line[1:] if len(x) > 0]
split_line = lines[1].split(' ')
distances = [int(x.strip()) for x in split_line[1:] if len(x) > 0]

all_margins = []
for time, distance in zip(times, distances):
    curr_margins = []
    for charge_time in range(1, time-1):
        run_time = time - charge_time
        if charge_time * run_time > distance:
            curr_margins.append(charge_time)
    all_margins.append(curr_margins)

result = len(all_margins[0])
for margins in all_margins[1:]:
    result *= len(margins)

print(result)