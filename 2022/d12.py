import os.path
import time
from collections import defaultdict


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.nodes = defaultdict(set)
        self.visited = []

    def add_node(self, u, v):
        self.nodes[u].add(v)


def find_neighbors(x, y, rows, cols):
    return [
        (x0, y0)
        for x0 in range(x - 1, x + 2)
        for y0 in range(y - 1, y + 2)
        if (
            (x != x0 or y != y0)
            and (0 <= x0 < rows)
            and (0 <= y0 < cols)
            and abs(x0 - x + y0 - y) == 1
        )
    ]


def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph.nodes[last_node]

        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


def part1(data):
    g = Graph(len(data) * len(data[0]))
    rows = len(data)
    cols = len(data[0])
    start = end = None
    neighbors = defaultdict(list)
    for i in range(rows):
        for j in range(cols):
            neighbor = find_neighbors(i, j, rows, cols)
            char = data[i][j]
            elevation = ord(char) - 96

            if char == "S":
                elevation = 1
                start = (i, j)
            if char == "E":
                elevation = 26
                end = (i, j)
            for n in neighbor:
                char = data[n[0]][n[1]]
                if char == "S":
                    target_elevation = 1
                elif char == "E":
                    target_elevation = 26
                else:
                    target_elevation = ord(char) - 96
                if target_elevation - 1 <= elevation:
                    g.add_node((i, j), n)
                    neighbors[(i, j)].append(n)
    return len(shortest_path(g, start, end)) - 1


def part2(data):
    g = Graph(len(data) * len(data[0]))
    rows = len(data)
    cols = len(data[0])
    starts = []
    neighbors = defaultdict(list)
    for i in range(rows):
        for j in range(cols):
            neighbor = find_neighbors(i, j, rows, cols)
            char = data[i][j]
            elevation = ord(char) - 96
            if char == "S":
                elevation = 1
            elif char == "E":
                elevation = 26
                end = (i, j)
            if elevation == 1:
                starts.append((i, j))
            for n in neighbor:
                char = data[n[0]][n[1]]
                if char == "S":
                    target_elevation = 1
                elif char == "E":
                    target_elevation = 26
                else:
                    target_elevation = ord(char) - 96
                if target_elevation - 1 <= elevation:
                    g.add_node((i, j), n)
                    neighbors[(i, j)].append(n)

    distances = [len(shortest_path(g, start, end)) for start in starts]
    distances = [i - 1 for i in distances if i > 0]

    return min(distances)


if __name__ == "__main__":
    replit_start_time = time.perf_counter()

    with open(os.path.join(os.path.dirname(__file__), "d12.txt")) as f:
        data = f.read().splitlines()
        print(part1(data))
        print(part2(data))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
