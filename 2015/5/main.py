import os
import re

def solution1(data):
    vowels = 'aeiou'
    bad_chars = ['ab', 'cd', 'pq', 'xy']
    
    nice_strings = []
    for i in data:

        nice_string = [False, False, False]

        if len(re.findall(f'[{vowels}]', i)) >= 3:
            nice_string[0] = True

        if len(re.findall('|'.join(bad_chars), i)) == 0:
            nice_string[2] = True

        if len([match[0] for match in re.findall(r'((\w)\2{1,})', i)]) > 0:
            nice_string[1] = True

        if all(nice_string):
            nice_strings.append(i)

    return len(nice_strings)


def solution2(data):
    nice_strings = []
    for i in data:
        nice_string = [False, False]

        for n in range(len(i) - 3):
            if i[n: n +2] in i[n + 2:]:
                nice_string[0] = True
                break

        n = 2

        while n < len(i):
            if i[n-2] == i[n]:
                nice_string[1] = True
                break
            else:
                n += 1        
        if all(nice_string):
            nice_strings.append(i)
    return len(nice_strings)

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    print(solution1(data))
    print(solution2(data))