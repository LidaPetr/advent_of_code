import os.path
import time


def process(data):
    rocks = set()
    for d in data:
        points = d.split(" -> ")
        lines = []
        for p in points:
            s = p.split(",")
            lines.append((int(s[0]), int(s[1])))
        for i in range(len(lines) - 1):
            if lines[i][0] == lines[i + 1][0]:
                step = -1 if lines[i][1] > lines[i + 1][1] else 1
                for j in range(lines[i][1], lines[i + 1][1] + step, step):
                    rocks.add((lines[i][0], j))
            else:
                step = -1 if lines[i][0] > lines[i + 1][0] else 1
                for j in range(lines[i][0], lines[i + 1][0] + step, step):
                    rocks.add((j, lines[i][1]))
    return rocks


def part2(data):
    rocks = process(data)
    max_row = max([i[1] for i in rocks]) + 2
    total = 0
    while (500, 0) not in rocks:
        sand = [500, 0]
        while True:
            if sand[1] + 1 == max_row:
                total += 1
                rocks.add(tuple(sand))
                break
            if (sand[0], sand[1] + 1) not in rocks:
                sand[1] += 1
            elif (sand[0] - 1, sand[1] + 1) not in rocks:
                sand[0] -= 1
                sand[1] += 1
            elif (sand[0] + 1, sand[1] + 1) not in rocks:
                sand[0] += 1
                sand[1] += 1
            else:
                total += 1
                rocks.add(tuple(sand))
                break

    return total


def part1(data):
    rocks = process(data)
    max_row = max([i[1] for i in rocks])
    total = 0
    hold = True
    while hold:
        sand = [500, 0]
        while True:
            if (sand[0], sand[1] + 1) not in rocks:
                sand[1] += 1
            elif (sand[0] - 1, sand[1] + 1) not in rocks:
                sand[0] -= 1
                sand[1] += 1
            elif (sand[0] + 1, sand[1] + 1) not in rocks:
                sand[0] += 1
                sand[1] += 1
            else:
                total += 1
                rocks.add(tuple(sand))
                break
            if sand[1] >= max_row:
                hold = False
                break

    return total


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "d14.txt")) as f:
        data = f.read().splitlines()
        print(part1(data))
        print(part2(data))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
