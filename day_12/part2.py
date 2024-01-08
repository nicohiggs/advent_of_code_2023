from functools import cache

# needed to look up some hints to solve this one. My part 1 brute force epicly failed here
# needed to try a recursive solution
# I learned about functools @cache for these large recursive problems!
# way easier than my own hand-rolled memoization...

@cache
def matches(springs, spring_len, records):
    if len(records) == 0:
        if all(char in '?.' for char in springs):
            return 1
        else:
            return 0

    curr_dam = records[0]
    rem_rec = records[1:]
    rem_dam = sum(rem_rec) + len(rem_rec)

    result = 0
    for prev_chars in range(spring_len - curr_dam - rem_dam + 1):
        candidate = '.' * prev_chars + '#' * curr_dam + '.'
        if all(s == c or s=='?' for s, c in zip(springs, candidate)):
            result += matches(springs[len(candidate):],
                              spring_len - curr_dam - prev_chars - 1,
                              rem_rec)

    return result

with open("input.txt") as f:
    lines = f.readlines()

result = 0
for line in lines:
    springs, records = line.strip().split(' ')
    records = [int(x) for x in records.split(',')]
    base_spring = springs + '?'
    springs = base_spring * 5
    springs = springs[:-1]
    records = records * 5
    result += matches(springs, len(springs), tuple(records))

print(result)