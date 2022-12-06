import os


def solution1(data):
    i = 4

    while i < len(data):
        if len(set(data[i-4:i])) == 4:
            return i
        else:
            i += 1

    return None


def solution2(data):
    i = 14

    while i < len(data):
        if len(set(data[i-14:i])) == 14:
            return i
        else:
            i += 1

    return None


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(f'Part 1: {solution1(data[0])}')
    print(f'Part 2: {solution2(data[0])}')