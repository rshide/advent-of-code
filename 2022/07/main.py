import os
from collections import defaultdict


def solution1(data):

    dir_totals = defaultdict(int)
    path = []

    for c in data:
        match c.split():
            case ['$', 'cd', '..']:
                path.pop()
            case ['$', 'cd', d]:
                # create stack of current path
                path.append(d)
            case ['$', 'ls']:
                pass
            case ['dir', d]:
                pass
            case [s,f]:
                # add to current path
                dir_totals[tuple(path)] += int(s)
                
                # recursively add to every parent path
                cur_path = path[:-1]
                while cur_path:
                    dir_totals[tuple(cur_path)] += int(s)
                    cur_path.pop()

    total = sum([c for c in dir_totals.values() if c <= 100000])

    return total


def solution2(data):

    dir_totals = defaultdict(int)
    path = []

    for c in data:
        match c.split():
            case ['$', 'cd', '..']:
                path.pop()
            case ['$', 'cd', d]:
                path.append(d)
            case ['$', 'ls']:
                pass
            case ['dir', d]:
                pass
            case [s,f]:
                dir_totals[tuple(path)] += int(s)
                cur_path = path[:-1]
                while cur_path:
                    dir_totals[tuple(cur_path)] += int(s)
                    cur_path.pop()

    TOTAL_AVAILABLE = 70000000
    FREE_SPACE = TOTAL_AVAILABLE - dir_totals[tuple('/')]
    SPACE_REQUIRED = 30000000
    SPACE_NEEDED = SPACE_REQUIRED - FREE_SPACE

    # find smallest directory that can be deleted
    min = SPACE_REQUIRED
    for d,s in dir_totals.items():
        if SPACE_NEEDED <= s <= min:
            min = s

    return min


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(f'Part 1: {solution1(data)}')
    print(f'Part 2: {solution2(data)}')