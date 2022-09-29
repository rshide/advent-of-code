import os
import re


def solution1(data):
    matrix = [[False for __ in range(1000)] for _ in range(1000)]

    for c in cleaned_data:
        for x in range(c[1][0], c[2][0] + 1):
            for y in range(c[1][1], c[2][1] + 1):
                if c[0] == "turn on":
                    matrix[x][y] = True
                elif c[0] == "turn off":
                    matrix[x][y] = False
                elif c[0] == "toggle":
                    matrix[x][y] = not matrix[x][y]

    lights_on = 0
    for r in matrix:
        lights_on += sum(r)

    return lights_on


def solution2(data):
    matrix = [[0 for __ in range(1000)] for _ in range(1000)]

    for c in cleaned_data:
        for x in range(c[1][0], c[2][0] + 1):
            for y in range(c[1][1], c[2][1] + 1):
                if c[0] == "turn on":
                    matrix[x][y] += 1
                elif c[0] == "turn off":
                    matrix[x][y] = max(0, matrix[x][y] - 1)
                elif c[0] == "toggle":
                    matrix[x][y] += 2
    lights_on = 0
    for r in matrix:
        lights_on += sum(r)

    return lights_on


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    instr = ["turn on", "turn off", "toggle"]

    cleaned_data = []
    for d in data:
        command = re.search("|".join(instr), d).group()
        coordinates = [
            [int(c) for c in p.strip().split(",")]
            for p in d[len(command) :].split("through")
        ]
        cleaned_data.append([command] + coordinates)

    print(solution1(cleaned_data))
    print(solution2(cleaned_data))
