import re


def game_reader(line):
    number_finder = re.compile("\d+")

    pos_colon = line.find(":")
    pos_pipe = line.find("|")

    winning_numbers = re.findall(number_finder, line[pos_colon:pos_pipe])
    lottery_numbers = re.findall(number_finder, line[pos_pipe:])

    winning_numbers = list(map(int, winning_numbers))
    lottery_numbers = list(map(int, lottery_numbers))

    return winning_numbers, lottery_numbers

def part1(winning_numbers, lottery_numbers):
    winners = 0
    for winning_number in winning_numbers:
        if winning_number in lottery_numbers:
            winners += 1

    if winners:
        points = 1 * 2 ** (winners-1)
    else:
        points = 0

    return points


def part2(winning_numbers, lottery_numbers, current_copies):
    winners = 0
    for winning_number in winning_numbers:
        if winning_number in lottery_numbers:
            winners += 1

    number_of_cards = 1
 #   for idx, copy in enumerate(current_copies):

    copies_to_keep = []
    for idx, copy in enumerate(current_copies):
        number_of_cards += copy[2]
        copy[1] += 1
        if copy[1] < copy[0]:
            copies_to_keep.append(idx)

    total_number_of_cards = sum(list(copy[2] for copy in current_copies)) + 1

    cleaned_copies = list(current_copies[i] for i in copies_to_keep)

    if winners:
        cleaned_copies.append([winners, 0, number_of_cards])

    print(total_number_of_cards, cleaned_copies)

    return cleaned_copies, total_number_of_cards


file = open("input.txt")

line = file.readline()
ii = 1
total_points = 0
total_cards = 0
current_copies = []
while line:
    winning_numbers, lottery_numbers = game_reader(line)
    total_points += part1(winning_numbers, lottery_numbers)
    current_copies, cards = part2(winning_numbers, lottery_numbers, current_copies)
    total_cards += cards
    line = file.readline()

print(f"Part 1: Total Points = {total_points}")
print(f"Part 2: Total Cards = {total_cards}")
