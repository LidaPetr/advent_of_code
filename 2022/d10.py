import os.path
import time


def check_cycle(cycle, x):
    if (cycle - 20) % 40 == 0:
        return cycle * x
    return 0


def part1(data):
    cycle = 1
    x = 1
    strengths = 0
    for line in data:
        strengths += check_cycle(cycle, x)
        if "addx" in line:
            value = int(line.split()[1])
            cycle += 1
            strengths += check_cycle(cycle, x)
            x += value
        cycle += 1
    return strengths


def draw_pixel(cycle, x, output_line, output):
    position = (cycle - 1) % 40
    if position in range(x - 1, x + 2):
        output[output_line] += "#"
    else:
        output[output_line] += "."
    return output


def part2(data):
    cycle = 1
    x = 1
    output = ["", "", "", "", "", ""]
    output_line = 0
    for line in data:
        output = draw_pixel(cycle, x, output_line, output)
        if "addx" in line:
            value = int(line.split()[1])
            cycle += 1
            if (cycle - 1) % 40 == 0:
                output_line += 1
            output = draw_pixel(cycle, x, output_line, output)
            x += value
        cycle += 1
        if (cycle - 1) % 40 == 0:
            output_line += 1
    return output


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "d10.txt")) as f:
        data = f.read().splitlines()
        print(part1(data))
        output = part2(data)
        for line in output:
            print(line)

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
