import sys
import re
import datetime
import multiprocessing as mp
import time


class Mapper:
    def __init__(self):
        self.maps = []

    def add_map(self, source_name, destination_name, ranges):
        self.maps.append({"source": source_name, "destination": destination_name, "ranges": ranges})

    def get_destination(self, source, source_name):
        current_map = next((item for item in self.maps if item["source"] == source_name), None)
        if current_map is not None:
            destination = sys.maxsize
            destination_found = False
            for combination in current_map['ranges']:
                if combination[1] <= source < (combination[1] + combination[2]) and combination[0] < destination:
                    destination = combination[0] + (source - combination[1])
                    destination_found = True

            if not destination_found:
                destination = source

            # print(f"{source_name}: {source} \t{current_map['destination']}: {destination}")

            source = self.get_destination(destination, current_map['destination'])

        return source


number_finder = re.compile("\d+")
category_finder = re.compile("(?P<source_name>\w+)-to-(?P<destination_name>\w+)")
def part1():
    #open file, get the list of seeds, then proceed until the ext non-empty line
    file = open("input.txt")
    line = file.readline()
    seed_list = list(map(int, re.findall(number_finder, line)))

    mapper = Mapper()

    while line:
        source_name = "NULL"
        destination_name = "NULL"
        ranges = []
        if re.match(category_finder, line):
            m = re.match(category_finder, line)
            source_name = m.group("source_name")
            destination_name = m.group("destination_name")

            line = file.readline()
            while line != "\n" and line:
                ranges.append(list(map(int, re.findall(number_finder, line))))
                line = file.readline()

        if source_name != "NULL":
            # print(source_name + " to " + destination_name + "\n", ranges)
            mapper.add_map(source_name, destination_name, ranges)
        line = file.readline()

    locations = []

    for seed in seed_list:
        locations.append(mapper.get_destination(seed, "seed"))

    print(f"The lowest value is: {min(locations)}")


def part2(mapper, seed_range):
    temp_location = sys.maxsize
    print(f"Starting seed range {seed_range[0]} to {seed_range[0] + seed_range[1]}")
    for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
        destination = mapper.get_destination(seed, "seed")
        if destination < temp_location:
            temp_location = destination
        # print(f"{((seed-seed_range[0])/seed_range[1]):.2%}", end="\r")
    print(f"Completed with seed range {seed_range[0]} to {seed_range[0] + seed_range[1]}")
    return temp_location


if __name__ == '__main__':
    start_time = time.perf_counter()
    # open file, get the list of seeds, then proceed until the ext non-empty line
    file = open("input.txt")
    line = file.readline()
    seed_raw = list(map(int, re.findall(number_finder, line)))

    seed_list = []
    for ii in range(int(len(seed_raw) / 2)):
        seed_list.append([seed_raw[2 * ii], seed_raw[2 * ii + 1]])

    mapper = Mapper()

    while line:
        source_name = "NULL"
        destination_name = "NULL"
        ranges = []
        if re.match(category_finder, line):
            m = re.match(category_finder, line)
            source_name = m.group("source_name")
            destination_name = m.group("destination_name")

            line = file.readline()
            while line != "\n" and line:
                ranges.append(list(map(int, re.findall(number_finder, line))))
                line = file.readline()

        if source_name != "NULL":
            # print(source_name + " to " + destination_name + "\n", ranges)
            mapper.add_map(source_name, destination_name, ranges)
        line = file.readline()

    pool = mp.Pool(10)

    processes = [pool.apply_async(part2, args=(mapper, x)) for x in seed_list]

    result = [p.get() for p in processes]

    print(result)

    print(f"The lowest value is: {min(result)}")
    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")
