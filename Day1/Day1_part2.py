import re

def mapnumbers(matches):
    for idx, x in enumerate(matches):
        match x:
            case "one" | "ne":
                matches[idx] = "1"
            case "two" | "wo":
                matches[idx] = "2"
            case "three":
                matches[idx] = "3"
            case "four":
                matches[idx] = "4"
            case "five":
                matches[idx] = "5"
            case "six":
                matches[idx] = "6"
            case "seven":
                matches[idx] = "7"
            case "eight" | "ight":
                matches[idx] = "8"
            case "nine" | "ine":
                matches[idx] = "9"
    return matches


def getnumbers(passcode):
    pattern = re.compile("\d|one|(?<=two)ne|(?<=eight)wo|two|three|four|five|six|seven|(?<=one)ight|(?<=three)ight|(?<=five)ight|(?<=nine)ight|eight|(?<=seven)ine|nine")
    matches = pattern.findall(passcode)
    matches = mapnumbers(matches)

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