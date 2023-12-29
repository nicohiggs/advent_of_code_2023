with open("input.txt") as f:
    lines = f.readlines()

split_line = lines[0].split(' ')
times = [x.strip() for x in split_line[1:] if len(x) > 0]
total_time = ''
for time in times:
    total_time += time
total_time = int(total_time)
print(total_time)
split_line = lines[1].split(' ')
distances = [x.strip() for x in split_line[1:] if len(x) > 0]
total_distance = ''
for distance in distances:
    total_distance += distance
total_distance = int(total_distance)
print(total_distance)

margins = []
for charge_time in range(1, total_time-1):
    run_time = total_time - charge_time
    if charge_time * run_time > total_distance:
        margins.append(charge_time)

result = len(margins)

print(result)