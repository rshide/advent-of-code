import os
import json


def solution1(data):
    total = 0
    for d in data:
        if type(d) == int:
            total += d
        elif type(d) == dict:
            

    return None


def solution2(data):
    return None


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = json.load(file)

    print(solution1(data))
    print(solution2(data))
