import os


def solution1(data):

    count = 0

    for n in data:
        # clean up inputs
        e = tuple(tuple(int(v) for v in i.split('-')) for i in n.split(','))

        if ((e[0][0] >= e[1][0] and e[0][1] <= e[1][1]) or
            (e[0][0] <= e[1][0] and e[0][1] >= e[1][1])):
            count += 1

    return count


def solution2(data):
    count = 0

    for n in data:
        # clean up inputs
        e = tuple(tuple(int(v) for v in i.split('-')) for i in n.split(','))

        # split into ranges and compare for matches
        ranges = [[n for n in range(i[0], i[1]+1)] for i in e]
        if len(set(ranges[0]) & set(ranges[1])) > 0:
            count += 1

    return count

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(f'Part 1: {solution1(data)}')
    print(f'Part 2: {solution2(data)}')