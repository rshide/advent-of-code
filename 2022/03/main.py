import os
import string

def solution1(data):

    letters = dict(zip(string.ascii_letters, range(1,53)))
    total = 0

    for i in data:
        # split into equal halves
        front = i[:len(i)//2]
        back = i[len(i)//2:]

        # find common items
        common = list(set([l for l in front if l in back]))

        total += sum([letters[i] for i in common])

    return total


def solution2(data):

    letters = dict(zip(string.ascii_letters, range(1,53)))
    total = 0
    i = 0

    while i < len(data) - 1:
        
        # capture groups of 3
        group = data[i:i+3]

        # find like items
        common = list(set([l for l in group[0] if l in group[1] and l in group[2]]))

        total += sum([letters[i] for i in common])

        i += 3

    return total


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(f'Part 1: {solution1(data)}')
    print(f'Part 2: {solution2(data)}')