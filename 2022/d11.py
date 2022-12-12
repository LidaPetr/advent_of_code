import os.path
import time
import re
from collections import defaultdict
import math


def part(data, rounds=20, worry=3):
    monkeys = {}
    inspected = defaultdict(int)
    i = 0
    monkeys_order = []
    mod = 1
    while i < len(data):
        lines = data[i : i + 6]
        monkey = int(re.findall(r"\d+", lines[0])[0])
        monkeys_order.append(monkey)
        items = [int(i) for i in re.findall(r"\d+", lines[1])]
        operation = lines[2].split("= ")[-1]
        test = int(re.findall(r"\d+", lines[3])[0])
        throw_t = int(re.findall(r"\d+", lines[4])[0])
        throw_f = int(re.findall(r"\d+", lines[5])[0])
        monkeys[monkey] = {
            "items": items,
            "operation": operation,
            "test": test,
            "true": throw_t,
            "false": throw_f,
        }
        mod *= test
        i += 7
    for _ in range(rounds):
        for monkey in monkeys_order:
            target = monkeys[monkey]
            items = monkeys[monkey]["items"]
            inspected[monkey] += len(items)
            new = [eval(target["operation"]) // worry % mod for old in items]
            divisible = target["test"]
            monkeys[target["true"]]["items"].extend(
                [i for i in new if i % divisible == 0]
            )
            monkeys[target["false"]]["items"].extend(
                [i for i in new if i % divisible != 0]
            )
            monkeys[monkey]["items"] = []

    print(inspected)
    return math.prod(list(sorted(inspected.values()))[-2:])


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "d11.txt")) as f:
        data = f.read().splitlines()
        print(part(data))
        print(part(data, 10000, 1))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
