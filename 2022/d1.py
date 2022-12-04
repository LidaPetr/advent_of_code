import time


def d1_p1(numbers):
    count = 0
    max_calories = 0
    for number in numbers:
        if number:
            count += int(number)
            if count > max_calories:
                max_calories = count
        else:
            count = 0
    return max_calories


def d1(numbers, top):
    count = 0
    calories = []
    for number in numbers:
        if number:
            count += int(number)
        else:
            calories.append(count)
            count = 0
    if count:
        calories.append(count)
    calories.sort(reverse=True)
    return sum(calories[:top])


if __name__ == "__main__":
    replit_start_time = time.perf_counter()
    with open("d1.txt") as f:
        data = f.readlines()
    numbers = [x.strip() for x in data]

    print(d1(numbers, 1))
    print(d1(numbers, 3))

    # Keep this line at the end of your code
    replit_end_time = time.perf_counter()
    print("Elapsed time:", replit_end_time - replit_start_time)
