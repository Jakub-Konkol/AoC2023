# This is a sample Python script.
import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def getnumbers(passcode):
    pattern = re.compile("\d")
    matches = pattern.findall(passcode)
    if len(matches) > 1:
        combined = ''.join(matches[::len(matches)-1])
    elif len(matches) == 1:
        combined = matches[0] + matches[0]
    else:
        combined = 0
    return int(combined)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total = 0
    file = open("test_codes.txt")
    line = file.readline()
    while line:
        total += getnumbers(line)
        line = file.readline()
    print(total)