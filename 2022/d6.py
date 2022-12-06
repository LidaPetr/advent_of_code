import copy
import re
import time
from collections import deque


def d6(packet, marker_len):
    i = marker_len
    packet_len = len(packet)
    while i <= packet_len:
        marker = packet[i - marker_len : i]
        if len(set(marker)) == marker_len:
            return i
        i += 1
    return None


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("d6.txt") as f:
        line = f.readline().strip()

    print(d6(line, 4))
    print(d6(line, 14))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
