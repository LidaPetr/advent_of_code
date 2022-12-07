from collections import defaultdict
import time


def get_listed_items(data, i):
    dirs = []
    size = 0

    while i < len(data):
        line = data[i].strip()
        if line.startswith("$"):
            break
        parts = line.split()
        if line.startswith("dir"):
            dirs.append(parts[-1])
        else:
            size += int(parts[0])
        i += 1
    return dirs, size, i


def d7_p1(data):
    current_dir = "/"
    parent = {"/": None}
    parents = defaultdict(set)
    sizes = defaultdict(int)
    i = 1
    while i < len(data):
        line = data[i].strip()
        if line.startswith("$ ls"):
            child_dirs, size, i = get_listed_items(data, i + 1)
            for c in child_dirs:
                path = f"{current_dir}/{c}"
                parent[path] = current_dir
                parents[path].add(current_dir)
                parents[path].update(parents[current_dir])
            sizes[current_dir] = size
            for p in parents[current_dir]:
                sizes[p] += size
        elif line.startswith("$ cd"):
            parts = line.split()
            new_dir = parts[-1]
            if new_dir == "..":
                current_dir = parent[current_dir]
            else:
                current_dir = f"{current_dir}/{new_dir}"
            i += 1
    return sizes


def d7_p2(sizes):
    filesystem_space = 70000000
    space_needed = 30000000
    unused_space = filesystem_space - sizes["/"]
    extra_space = space_needed - unused_space
    return min([value for value in sizes.values() if value >= extra_space])


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("d7.txt") as f:
        data = f.readlines()

    sizes = d7_p1(data)
    print(sum([value for value in sizes.values() if value <= 100000]))
    print(d7_p2(sizes))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
