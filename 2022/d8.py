import os.path
import time


def find_grid(x, y, data):
    rows = len(data)
    cols = len(data[0])
    return [
        [data[x0][y] for x0 in range(x - 1, -1, -1)],
        [data[x0][y] for x0 in range(x + 1, rows)],
        [data[x][y0] for y0 in range(y - 1, -1, -1)],
        [data[x][y0] for y0 in range(y + 1, cols)],
    ]


def is_visible(x, y, data):
    grids = find_grid(x, y, data)
    if any(len(grid) == 0 for grid in grids):
        return True
    return any(max(grid) < data[x][y] for grid in grids)


def trees_number(x, y, data):
    grids = find_grid(x, y, data)
    target_tree = data[x][y]
    score = 1
    for grid in grids:

        if not len(grid):
            return 0
        distance = 0
        for i in grid:
            distance += 1
            if i >= target_tree:
                break
        score = score * distance

    return score


def part1(data):
    mins = []
    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_visible(i, j, data):
                count += 1
                mins.append((i, j))
    return count


def part2(data):
    scores = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            scores.append(trees_number(i, j, data))
    return max(scores)


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "d8.txt")) as f:
        data = [[int(char) for char in line] for line in f.read().splitlines()]
        print(part1(data))
        print(part2(data))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
