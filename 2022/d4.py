import time


def d4_p1(pairs):
    def segments_convert(segm):
        total = segm.split("-")
        start = int(total[0])
        end = int(total[1]) + 1
        return set(range(start, end))

    count = 0
    for pair in pairs:
        segments = pair.split(",")
        first = segments_convert(segments[0])
        second = segments_convert(segments[1])
        if not first.difference(second) or not second.difference(first):
            count += 1

    return count


def d4_p2(pairs):
    def segments_convert(segm):
        total = segm.split("-")
        start = int(total[0])
        end = int(total[1]) + 1
        return set(range(start, end))

    count = 0
    for pair in pairs:
        segments = pair.split(",")
        first = segments_convert(segments[0])
        second = segments_convert(segments[1])
        if first.intersection(second):
            count += 1

    return count


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("d4.txt") as f:
        data = f.readlines()
    pairs = [x.strip() for x in data]

    print(d4_p1(pairs))
    print(d4_p2(pairs))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
