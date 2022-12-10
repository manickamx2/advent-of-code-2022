########## PART 1 ##########
from collections import deque
import re


def read_initial_configuration():
    with open('day5-input.txt') as f:
        lines = f.readlines()

    stack_data = {str(x): deque() for x in range(1, 10)}

    idx = 0
    line = lines[idx]
    while not line.strip().startswith('1'):
        col = 1
        space_count = 0
        for char in line:
            if char == '\n':
                break
            elif char.isalpha():
                stack_data[str(col)].append(char)
                col += 1
                space_count = 0
            else:
                if char == ' ':
                    space_count += 1
                if space_count == 4:
                    space_count = 0
                    col += 1
        idx += 1
        line = lines[idx]

    # advance to first line of moving instructions
    while not line.strip().startswith('move'):
        idx += 1
        line = lines[idx]

    # rearrange crates
    while idx < len(lines):
        n = re.findall("\d+", lines[idx])
        amount, src, dest = n[0], n[1], n[2]
        a = 0
        while a < int(amount):
            crate = stack_data[src].popleft()
            stack_data[dest].appendleft(crate)
            a += 1
        idx += 1

    # get the topmost crates as our answer
    crates = ''
    for col in stack_data:
        crates += stack_data[col].popleft()

    return crates


crates = read_initial_configuration()
print(f"part 1 answer: {crates}")


