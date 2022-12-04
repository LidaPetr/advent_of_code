import time

moves_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
scores = {"rock": 1, "paper": 2, "scissors": 3}
winners = {"paper": "rock", "scissors": "paper", "rock": "scissors"}
losers = {"rock": "paper", "paper": "scissors", "scissors": "rock"}


def d2_p1(moves):
    total_score = 0
    for move in moves:
        i = move.split()
        elf = moves_map[i[0]]
        me = moves_map[i[1]]
        total_score += scores[me]
        if elf != me:
            if winners[me] == elf:
                total_score += 6
        else:
            total_score += 3
    return total_score


def d2_p2(moves):
    total_score = 0
    for move in moves:
        i = move.split()
        elf = moves_map[i[0]]
        if i[1] == "X":
            total_score += scores[winners[elf]]
        elif i[1] == "Y":
            total_score += 3 + scores[elf]
        else:
            total_score += 6 + scores[losers[elf]]
    return total_score


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("d2.txt") as f:
        data = f.readlines()
    moves = [x.strip() for x in data]
    print(d2_p1(moves))
    print(d2_p2(moves))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
