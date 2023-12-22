with open("input.txt") as f:
    lines = f.readlines()

seeds_str = lines[0].split(':')[1].strip().split(' ')
seeds = []
for seed in seeds_str:
    seeds.append(int(seed))

seed2soil = []
soil2fert = []
fert2water = []
water2light = []
light2temp = []
temp2humd = []
humd2loc = []

line_num = 2
while(line_num < len(lines)):
    curr_line = lines[line_num].strip()

    if curr_line == "seed-to-soil map:":
        line_num += 1
        curr_line = lines[line_num].strip()
        while(len(curr_line) > 0):
            des_start, src_start, range_l = curr_line.split(' ')
            seed2soil.append({
                "des_start":int(des_start),
                "src_start":int(src_start),
                "range_l":int(range_l)
            })
            line_num += 1
            curr_line = lines[line_num].strip()
    elif curr_line == "soil-to-fertilizer map:":
        line_num += 1
        curr_line = lines[line_num].strip()
        while(len(curr_line) > 0):
            des_start, src_start, range_l = curr_line.split(' ')
            soil2fert.append({
                "des_start":int(des_start),
                "src_start":int(src_start),
                "range_l":int(range_l)
            })
            line_num += 1
            curr_line = lines[line_num].strip()
    elif curr_line == "fertilizer-to-water map:":
        line_num += 1
        curr_line = lines[line_num].strip()
        while(len(curr_line) > 0):
            des_start, src_start, range_l = curr_line.split(' ')
            fert2water.append({
                "des_start":int(des_start),
                "src_start":int(src_start),
                "range_l":int(range_l)
            })
            line_num += 1
            curr_line = lines[line_num].strip()
    elif curr_line == "water-to-light map:":
        line_num += 1
        curr_line = lines[line_num].strip()
        while(len(curr_line) > 0):
            des_start, src_start, range_l = curr_line.split(' ')
            water2light.append({
                "des_start":int(des_start),
                "src_start":int(src_start),
                "range_l":int(range_l)
            })
            line_num += 1
            curr_line = lines[line_num].strip()
    elif curr_line == "light-to-temperature map:":
        line_num += 1
        curr_line = lines[line_num].strip()
        while(len(curr_line) > 0):
            des_start, src_start, range_l = curr_line.split(' ')
            light2temp.append({
                "des_start":int(des_start),
                "src_start":int(src_start),
                "range_l":int(range_l)
            })
            line_num += 1
            curr_line = lines[line_num].strip()
    elif curr_line == "temperature-to-humidity map:":
        line_num += 1
        curr_line = lines[line_num].strip()
        while(len(curr_line) > 0):
            des_start, src_start, range_l = curr_line.split(' ')
            temp2humd.append({
                "des_start":int(des_start),
                "src_start":int(src_start),
                "range_l":int(range_l)
            })
            line_num += 1
            curr_line = lines[line_num].strip()
    elif curr_line == "humidity-to-location map:":
        line_num += 1
        curr_line = lines[line_num].strip()
        while(len(curr_line) > 0):
            des_start, src_start, range_l = curr_line.split(' ')
            humd2loc.append({
                "des_start":int(des_start),
                "src_start":int(src_start),
                "range_l":int(range_l)
            })
            line_num += 1
            if line_num >= len(lines):
                break
            curr_line = lines[line_num].strip()
    else:
        line_num += 1


def find_corresponding_num(curr_val, s_maps):
    for s_map in s_maps:
        des_start = s_map["des_start"]
        src_start = s_map["src_start"]
        range_l = s_map["range_l"]
        if curr_val >= src_start and curr_val < src_start + range_l:
            return (curr_val - src_start) + des_start
    return curr_val

locations = []
for seed in seeds:
    curr_val = seed
    curr_val = find_corresponding_num(curr_val, seed2soil)
    curr_val = find_corresponding_num(curr_val, soil2fert)
    curr_val = find_corresponding_num(curr_val, fert2water)
    curr_val = find_corresponding_num(curr_val, water2light)
    curr_val = find_corresponding_num(curr_val, light2temp)
    curr_val = find_corresponding_num(curr_val, temp2humd)
    curr_val = find_corresponding_num(curr_val, humd2loc)
    locations.append(curr_val)

print(min(locations))
