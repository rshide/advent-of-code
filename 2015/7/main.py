import os
import collections


def solution1(data):

    m = {}

    for d in data:
        if "AND" in d[0] and m.get(d[0][0]) and m.get(d[0][2]):
            m[d[1]] = m.get(d[0][0]) & m.get(d[0][2])
        elif "OR" in d[0] and m.get(d[0][0]) and m.get(d[0][2]):
            m[d[1]] = m.get(d[0][0]) | m.get(d[0][2])
        elif "LSHIFT" in d[0] and m.get(d[0][0]):
            m[d[1]] = m.get(d[0][0]) << d[0][2]
        elif "RSHIFT" in d[0] and m.get(d[0][0]):
            m[d[1]] = m.get(d[0][0]) >> d[0][2]
        elif "NOT" in d[0] and m.get(d[0][0]):
            m[d[1]] = ~m.get(d[0][0])

    od = collections.OrderedDict(sorted(m.items()))

    return od.get("a")


def solution2(data):
    return None


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    cleaned_data = [d.split("->") for d in data]

    cleaned_data = []
    for d in data:
        temp = d.split("->")
        command = temp[0].strip().split(" ")
        assignment = temp[1].strip()
        cleaned_data.append([command, assignment])

    print(solution1(cleaned_data))
    print(solution2(data))
