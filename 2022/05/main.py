import os
import re

def solution1(data):

    layout = []
    split = 0

    # build layout
    for r in data:
        if '[' not in r:
            break
        else:
            row = []
            i = 0

            while i < len(r):
                row.append(r[i:i+4].strip())
                i += 4
            layout.append(row)
        split += 1

    # transpose layout into stack
    transposed_tuples = list(zip(*layout))
    layout = [[v for v in reversed(sublist) if v] for sublist in transposed_tuples]

    # move split pointer to start of instructions
    split += 2

    for i in data[split:]:
        instr = [int(n) for n in re.findall(r'\d+', i)]

        # interate through the number of moves
        for _ in range(instr[0]):
            temp = layout[instr[1] - 1].pop()
            layout[instr[2] - 1].append(temp)
            
    regex = re.compile('[^a-zA-Z]')

    top = ''.join([regex.sub('', c[-1]) for c in layout])
    return top


def solution2(data):

    layout = []
    split = 0

    # build layout
    for r in data:
        if '[' not in r:
            break
        else:
            row = []
            i = 0

            while i < len(r):
                row.append(r[i:i+4].strip())
                i += 4
            layout.append(row)
        split += 1

    # transpose layout into stack
    transposed_tuples = list(zip(*layout))
    layout = [[v for v in reversed(sublist) if v] for sublist in transposed_tuples]

    # move split pointer to start of instructions
    split += 2

    for i in data[split:]:
        instr = [int(n) for n in re.findall(r'\d+', i)]

        # pop top N crates
        temp = layout[instr[1] - 1][-instr[0]:]
        del layout[instr[1] - 1][-instr[0]:]
        layout[instr[2] - 1] += temp

    regex = re.compile('[^a-zA-Z]')

    top = ''.join([regex.sub('', c[-1]) for c in layout]) 
    return top


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(f'Part 1: {solution1(data)}')
    print(f'Part 2: {solution2(data)}')