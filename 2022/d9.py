import os.path
import time


def sign(a):
    return (a > 0) - (a < 0)


def move_tail(h, t, axis):
    dis = h[axis] - t[axis]
    if abs(dis) > 1:
        t[axis] = t[axis] + sign(dis) * 1
    return t


def move_diagonal(h, t):
    for i in [0, 1]:
        t[i] = t[i] + sign(h[i] - t[i]) * 1
    return t


def check_distance(h, t):
    if h[0] != t[0] and h[1] != t[1]:
        if not t in [
            [h[0] + 1, h[1] + 1],
            [h[0] - 1, h[1] - 1],
            [h[0] + 1, h[1] - 1],
            [h[0] - 1, h[1] + 1],
        ]:
            t = move_diagonal(h, t)
    elif h[0] != t[0]:
        t = move_tail(h, t, 0)
    elif h[1] != t[1]:
        t = move_tail(h, t, 1)
    return t


def part1(data, knots):
    visited = set()
    directions = {"R": (1, 1), "U": (0, 1), "L": (1, -1), "D": (0, -1)}
    for line in data:
        step = line.split()
        direction = step[0]
        num = int(step[1])
        for _ in range(num):
            ax = directions[direction][0]
            value = directions[direction][1]
            knots[0][ax] = knots[0][ax] + value
            for i in range(1, len(knots)):
                knots[i] = check_distance(knots[i - 1], knots[i])
            visited.add(tuple(knots[-1]))

    return len(visited)


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "d9.txt")) as f:
        data = f.read().splitlines()
        two_knots = [[0, 0] for _ in range(2)]
        ten_knots = [[0, 0] for _ in range(10)]
        print(part1(data, two_knots))
        print(part1(data, ten_knots))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
