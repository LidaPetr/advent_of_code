import itertools
import math
import os.path
import re
import time

from collections import defaultdict, Counter


def monad(num,steps):
    variables = defaultdict(int)
    counter = 0
    for step in steps:
        if step[0] == 'inp':
            variables[step[1]] = int(num[counter])
            counter+=1
        else:
            first = variables[step[1]]
            second = int(step[2]) if step[2].lstrip("-").isdigit() else variables[step[2]]
            if step[0] == 'mul':
                variables[step[1]] *= second
            elif step[0] == 'eql':
                variables[step[1]] = 1 if first == second else 0
            elif step[0] == 'add':
                variables[step[1]] += second
            elif step[0] == 'div':
                if second == 0:
                    return 1
                variables[step[1]] //= second
            elif step[0] == 'mod':
                if variables[step[1]] < 0 or second <= 0:
                    return 1
                variables[step[1]] %= second
    print(num)
    print(variables)
    return variables['z']


def part1(steps):
    for num in range(11111111111111,99999999999999):
    #for num in range(99999999999999,11111111111110,-1):
        n = str(num)
        if not '0' in n:
            res = monad(n,steps)
            if not res:
                break
    return num


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    counter = 0
    for i in range(1,717):
        counter += len(str(i))
        print(i,counter)
        if counter >= 2040:
            print(i,counter)
            break
    print(counter)

    with open(os.path.join(os.path.dirname(__file__), "data.txt")) as f:
        data = [d.split() for d in f.read().splitlines()]
        #print(monad(str(99999999927392-7645130729),data))
        print(sum(int(digit) for digit in str(11111111119195)))

        #print(part1(data))
    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
