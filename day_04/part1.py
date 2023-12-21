with open("input.txt") as f:
    lines = f.readlines()

result = 0
for line in lines:
    split_line = line.split(":")[1]
    split_line = split_line.split("|")
    winning_numbers_str = split_line[0]
    my_numbers_str = split_line[1]

    winning_numbers_str = winning_numbers_str.split(' ')
    winning_numbers = []
    for number_str in winning_numbers_str:
        if len(number_str) > 0:
            winning_numbers.append(int(number_str))
    my_numbers_str = my_numbers_str.split(' ')
    my_numbers = []
    for number_str in my_numbers_str:
        if len(number_str) > 0:
            my_numbers.append(int(number_str))
    
    points = 0
    for number in my_numbers:
        for win_number in winning_numbers:
            if number == win_number:
                if points == 0:
                    points = 1
                else:
                    points *= 2
    result += points
    
print(result)
