import re

def extract_numbers(game):
    pattern_blue = re.compile('\d+(?=\sblue)')
    pattern_red = re.compile('\d+(?=\sred)')
    pattern_green = re.compile('\d+(?=\sgreen)')
    matches = game.split(';')
    valid = []
    for play in matches:
        val = []
        for pattern in [pattern_red, pattern_green, pattern_blue]:
            m = re.search(pattern, play)
            if m:
                val.append(int(m.group()))
            else:
                val.append(0)
        if val[0] <= 12 and val[1] <= 13 and val[2] <= 14:
            valid.append(True)
        else:
            valid.append(False)
    return all(valid)


if __name__ == '__main__':
    total = 0
    line_num = 0

    file = open("input.txt")
    line = file.readline()
    line_num += 1
    while line:
        if extract_numbers(line):
            total += line_num
        line = file.readline()
        line_num += 1

    print(total)