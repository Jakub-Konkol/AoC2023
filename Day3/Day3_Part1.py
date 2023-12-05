import numpy as np
import re


def boundary_crusher(desired, minimum, maximum):
    if desired < minimum:
        desired = minimum
    elif desired > maximum:
        desired = maximum
    return desired


def pos_list(start, end, line_min=0, line_max = 8):
    temp = []
    position = start - 1
    while position <= end:
        temp.append(boundary_crusher(position, line_min, line_max))
        position += 1
    return temp

values = []

file = open("input.txt")

number_finder = re.compile("\d+")
symbol_finder = re.compile("[^\.\d\n]")

current_line = file.readline()
next_line = file.readline()
previous_line = "." * len(current_line)

while next_line:
    print("Current line: " + current_line.strip())
    results = re.finditer(number_finder, current_line)

    for x in results:
        found_symbol = False
        start_pos = x.start()
        end_pos = x.end()

        search_list = pos_list(start_pos, end_pos, 0, len(current_line))

        # search previous line
        for position in search_list:
            if re.match(symbol_finder, previous_line[position]):
                found_symbol = True
                print(f"Matched {x.group()} with a symbol on the previous line")

        # search current line:
        for position in [search_list[0], search_list[-1]]:
            if re.match(symbol_finder, current_line[position]):
                found_symbol = True
                print(f"Matched {x.group()} with a symbol on the current line")

        # search next line:
        for position in search_list:
            if re.match(symbol_finder, next_line[position]):
                found_symbol = True
                print(f"Matched {x.group()} with a symbol on the next line")

        if found_symbol:
            values.append(int(x.group()))

    previous_line = current_line
    current_line = next_line
    next_line = file.readline()

# final line handling
next_line = "." * len(current_line)

print("Current line:" + current_line.strip())
results = re.finditer(number_finder, current_line)

for x in results:
    found_symbol = False
    start_pos = x.start()
    end_pos = x.end()

    search_list = pos_list(start_pos, end_pos, 0, len(current_line))

    # search previous line
    for position in search_list:
        if re.match(symbol_finder, previous_line[position]):
            found_symbol = True
            print(f"Matched {x.group()} with a symbol on the previous line")

    # search current line:
    for position in [search_list[0], search_list[-1]]:
        if re.match(symbol_finder, current_line[position]):
            found_symbol = True
            print(f"Matched {x.group()} with a symbol on the current line")

    # search next line:
    for position in search_list:
        if re.match(symbol_finder, next_line[position]):
            found_symbol = True
            print(f"Matched {x.group()} with a symbol on the next line")

    if found_symbol:
        values.append(int(x.group()))

file.close()

print(sum(values))