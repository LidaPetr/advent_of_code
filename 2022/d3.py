import time


def d3_p1(items):
    total_score = 0
    for item in items:
        size = int(len(item) / 2)
        first = set(item[:size])
        second = set(item[size:])
        both = first.intersection(second)
        rep = ord(list(both)[0])
        if rep < 97:
            total_score += rep - 38
        else:
            total_score += rep - 96
    return total_score


def d3_p2(items):
    total_score = 0
    for i in range(0, len(items), 3):
        first = set(items[i])
        second = set(items[i + 1])
        third = set(items[i + 2])
        badge = first.intersection(second.intersection(third))
        rep = ord(list(badge)[0])
        if rep < 97:
            total_score += rep - 38
        else:
            total_score += rep - 96
    return total_score


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("d3.txt") as f:
        data = f.readlines()
    items = [x.strip() for x in data]
    print(d3_p1(items))
    print(d3_p2(items))
    # print(d2_p1(moves))
    # print(d2_p2(moves))
    # print(d1(numbers,3))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
