import math
import re


def race_result_calculator(total_time, distance_to_beat):
    # old brute force method
    # time_spent_charging = 0
    # number_of_wins = 0
    #
    # while time_spent_charging < total_time:
    #     time_left_in_race = total_time - time_spent_charging
    #     boat_speed = time_spent_charging
    #
    #     distance_traveled = boat_speed * time_left_in_race
    #
    #     if distance_traveled > distance_to_beat:
    #         number_of_wins += 1
    #
    #     print(f"{time_spent_charging/total_time:.2%} completed", end="\r")
    #
    #     time_spent_charging += 1

    # non-brute force way
    start_win = math.ceil((total_time - math.sqrt(total_time ** 2 - 4 * distance_to_beat)) / 2)
    end_win = math.floor((total_time + math.sqrt(total_time ** 2 - 4 * distance_to_beat)) / 2)

    return end_win - start_win + 1


def part1(filename):
    number_finder = re.compile("\d+")
    file = open(filename)

    line = file.readline()
    race_times = re.findall(number_finder, line)
    race_times = list(map(int, race_times))

    line = file.readline()
    race_distances = re.findall(number_finder, line)
    race_distances = list(map(int, race_distances))
    file.close()

    results = 1

    for race_time, race_distance in zip(race_times, race_distances):
        results *= race_result_calculator(race_time, race_distance)

    print(results)


def part2(filename):
    number_finder = re.compile("\d+")
    file = open(filename)

    line = file.readline()
    race_times = re.findall(number_finder, line)
    race_times = int(''.join(race_times))

    line = file.readline()
    race_distances = re.findall(number_finder, line)
    race_distances = int(''.join(race_distances))
    file.close()

    results = race_result_calculator(race_times, race_distances)

    print(results)

if __name__ == '__main__':
    part2("input.txt")
