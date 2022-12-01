import os


def solution1(data):

    e = [] # list containing each elf's load
    tmp = [] # current elf's load

    m = 0
    for n in data:
        if n:
            tmp.append(int(n))
        else:
            e.append(tmp)
            total = sum(tmp)
            if total > m:
                m = total
            tmp = []

    if tmp:
        e.append(tmp)
        total = sum(tmp)
        if total > m:
            m = total

    return total


def solution2(data):
    e = [] # list containing each elf's load
    tmp = 0 # current elf's load

    for n in data:
        if n:
            tmp += int(n)
        else:
            e.append(tmp)
            tmp = 0
            
    if tmp:
        tmp += int(n)
        e.append(tmp)
  
    return sum(sorted(e)[-3:])


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(f'Part 1: {solution1(data)}')
    print(f'Part 2: {solution2(data)}')
