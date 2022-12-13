import os.path
import time
import re
from collections import defaultdict
import math


def check_ints(p1, p2):
    if p1 < p2:
        return True
    elif p1 > p2:
        return False
    else:
        return None


def check_lists(p1, p2):
    j = 0
    while j < len(p1) and j < len(p2):
        check = compare(p1[j], p2[j])
        if check is not None:
            return check
        j += 1
    if len(p1) < len(p2):
        return True
    elif len(p1) > len(p2):
        return False
    return None


def compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        return check_ints(p1, p2)
    elif isinstance(p1, int):
        p1 = [p1]
    elif isinstance(p2, int):
        p2 = [p2]

    return check_lists(p1, p2)


def part1(data):

    i = 0
    sum = 0
    pair = 1
    while i < len(data):
        if check_lists(data[i], data[i + 1]):
            sum += pair

        pair += 1
        i += 2

    return sum


def part2(data):

    data.append([[2]])
    data.append([[6]])

    n = len(data)
    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if check_lists(data[j + 1], data[j]):
                swapped = True
                data[j], data[j + 1] = data[j + 1], data[j]
        if not swapped:
            break
    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "d13.txt")) as f:
        data = [eval(line) for line in f.read().splitlines() if line]
        print(part1(data))
        print(part2(data))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
