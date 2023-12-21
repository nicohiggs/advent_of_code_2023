with open("input.txt") as f:
    lines = f.readlines()

cards = {}
for i in range(1, 219):
    cards[i] = 1

for curr_line, line in enumerate(lines):
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
    
    cards_won = 0
    curr_card = curr_line + 1
    for number in my_numbers:
        for win_number in winning_numbers:
            if number == win_number:
                cards_won += 1

    for i in range(curr_card + 1, curr_card + 1 + cards_won):
        cards[i] = cards[i] + cards[curr_card]

result = 0
for card in cards:
    result += cards[card]
    
print(result)