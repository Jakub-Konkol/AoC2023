import re
import numpy as np


def extract_numbers(game):
    #compile regex and split the game into individual matches
    pattern_blue = re.compile('\d+(?=\sblue)')
    pattern_red = re.compile('\d+(?=\sred)')
    pattern_green = re.compile('\d+(?=\sgreen)')
    matches = game.split(';')
    all_games_val = []

    for play in matches:
        val = []
        for pattern in [pattern_red, pattern_green, pattern_blue]:
            m = re.search(pattern, play)
            if m:
                val.append(int(m.group()))
            else:
                val.append(0)
        all_games_val.append(val)

    all_games = np.array(all_games_val)
    minimum_set = [all_games[:,x].max() for x in [0, 1, 2]]
    return minimum_set[0] * minimum_set[1] * minimum_set[2]

if __name__ == '__main__':
    total = 0
    line_num = 0

    file = open("input.txt")
    line = file.readline()
    line_num += 1
    while line:
        total += extract_numbers(line)
        line = file.readline()

    print(total)