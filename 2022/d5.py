import copy
import re
import time
from collections import deque


def d5_p1(initial_stacks, instructions, stacks_num):
    stacks = copy.deepcopy(initial_stacks)
    for instruction in instructions:
        number = int(instruction[0])
        stack_start = int(instruction[1])
        stack_end = int(instruction[2])

        for _ in range(number):
            crate = stacks[stack_start].pop()
            stacks[stack_end].append(crate)

    return "".join([stacks[i].pop() for i in range(1, stacks_num + 1)])


def d5_p2(initial_stacks, instructions, stacks_num):
    stacks = copy.deepcopy(initial_stacks)
    for instruction in instructions:
        number = int(instruction[0])
        stack_start = int(instruction[1])
        stack_end = int(instruction[2])

        crates_moved = []
        for _ in range(number):
            crates_moved.append(stacks[stack_start].pop())
        stacks[stack_end].extend(crates_moved[::-1])

    return "".join([stacks[i].pop() for i in range(1, stacks_num + 1)])


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("d5.txt") as f:

        # first section
        stacks = {}
        line = f.readline().strip("\n")
        stacks_num = int((len(line) + 1) / 4)
        stacks = {i: deque([]) for i in range(1, stacks_num + 1)}
        while not "1" in line:
            for n in range(stacks_num):
                if not line[4 * n + 1] == " ":
                    stacks[n + 1].appendleft(line[4 * n + 1])
            line = f.readline().strip("\n")

        # second section
        f.readline()
        instructions = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            instructions.append(re.findall(r"\d+", line))

    print(d5_p1(stacks, instructions, stacks_num))
    print(d5_p2(stacks, instructions, stacks_num))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
