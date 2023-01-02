########## PART 1 ##########
import math
from typing import List

RIGHT = 'R'
UP = 'U'
LEFT = 'L'
DOWN = 'D'

with open('day9-input.txt') as f:
    lines = f.readlines()


def compute_distance(p1: List, p2: List):
    x1, y1 = p1
    x2, y2 = p2
    d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return d


def move_tail(head: List, tail: List):
    distance = compute_distance(head, tail)
    if distance < 2:
        return tail

    if tail[0] < head[0]:
        tail[0] += 1
    elif tail[0] > head[0]:
        tail[0] -= 1

    if tail[1] < head[1]:
        tail[1] += 1
    elif tail[1] > head[1]:
        tail[1] -= 1

    return tail


# part 1
# knots = 1

# part 2
knots = 9

# initialize a 'visited' set for each knot
visited_map = {x + 1: set() for x in range(knots)}
positions = {x + 1: [0, 0] for x in range(knots)}

# H thru T all start at (0, 0)
# Key 1 is our H, Key 1/9 is our T
for i in range(knots):
    visited_map[i + 1].add((0, 0))

hx, hy = 0, 0

for line in lines:
    move = line.strip().split()
    direction, units = move[0], int(move[1])
    x_delta, y_delta = 0, 0
    x_target, y_target = hx, hy

    if direction == RIGHT:
        x_delta = 1
        x_target += units
    elif direction == UP:
        y_delta = 1
        y_target += units
    elif direction == LEFT:
        x_delta = -1
        x_target -= units
    elif direction == DOWN:
        y_delta = -1
        y_target -= units

    while hx != x_target:
        hx += x_delta
        prev = [hx, hy]

        for i in positions:
            # move the tail
            positions[i] = move_tail(prev, positions[i])
            prev = positions[i]
            visited_map[i].add(tuple(positions[i]))

    while hy != y_target:
        hy += y_delta
        prev = [hx, hy]

        for i in positions:
            # move the tail
            positions[i] = move_tail(prev, positions[i])
            prev = positions[i]
            visited_map[i].add(tuple(positions[i]))

print(f"Number of positions that the tail of the rope visited at least once: {len(visited_map[knots])}")
