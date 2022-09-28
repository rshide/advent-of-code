import os
import hashlib

def checker(data, val):
    x = 1
    while hashlib.md5(f"{data}{x}".encode()).hexdigest()[:len(val)] != val:
        x += 1
    return x - 1

def solution1(data):
    return checker(data, '00000')

def solution2(data):
    return checker(data, '000000')

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()[0]

    print(solution1(data))
    print(solution2(data))