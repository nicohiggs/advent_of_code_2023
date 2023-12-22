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

def get_seed_ranges(seed_ranges, s_maps):
    new_inter_ranges = []
    for s_map in s_maps:
        new_solo_ranges = []
        while seed_ranges:
            seed_range = seed_ranges.pop()
            before_range = (seed_range[0], min(seed_range[1], s_map["src_start"]))
            inter_range = (max(seed_range[0], s_map["src_start"]), min(seed_range[1], s_map["src_start"]+s_map["range_l"]))
            after_range = (max(seed_range[0], s_map["src_start"]+s_map["range_l"]), seed_range[1])
            if before_range[0] < before_range[1]:
                new_solo_ranges.append(before_range)
            if inter_range[0] < inter_range[1]:
                new_inter_ranges.append((inter_range[0] - s_map["src_start"] + s_map["des_start"], inter_range[1] - s_map["src_start"] + s_map["des_start"]))
            if after_range[0] < after_range[1]:
                new_solo_ranges.append(after_range)
        seed_ranges = new_solo_ranges
    return new_inter_ranges + seed_ranges

locations = []
for i in range(0, len(seeds), 2):
    start = seeds[i]
    length = seeds[i+1]
    seed_range = (start, start+length)
    seed_ranges = [seed_range]
    seed_ranges = get_seed_ranges(seed_ranges, seed2soil)
    seed_ranges = get_seed_ranges(seed_ranges, soil2fert)
    seed_ranges = get_seed_ranges(seed_ranges, fert2water)
    seed_ranges = get_seed_ranges(seed_ranges, water2light)
    seed_ranges = get_seed_ranges(seed_ranges, light2temp)
    seed_ranges = get_seed_ranges(seed_ranges, temp2humd)
    seed_ranges = get_seed_ranges(seed_ranges, humd2loc)
    locations.append(min(seed_ranges)[0])

print(min(locations))