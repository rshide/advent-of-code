import os

def solution1():
    return None

def solution2():
    return None

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(solution1())
    print(solution2())