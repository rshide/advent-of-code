import os


def solution1(data):
    return None


def solution2(data):
    return None


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(f'Part 1: {solution1(data)}')
    print(f'Part 2: {solution2(data)}')