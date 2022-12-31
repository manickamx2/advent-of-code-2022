########## PART 1 ##########
from typing import List

with open('day8-input.txt') as f:
    lines = f.readlines()


def is_visible(r: int, c: int, trees: List, height: int):

    # check if visible from the North
    north = True
    x = r
    while x > 0:
        if trees[x - 1][c] >= height:
            north = False
            break
        x -= 1
    if north:
        return True

    # check if visible from the South
    south = True
    x = r
    while x < ROWS - 1:
        if trees[x + 1][c] >= height:
            south = False
            break
        x += 1
    if south:
        return True

    # check if visible from the East
    east = True
    y = c
    while y < COLS - 1:
        if trees[r][y + 1] >= height:
            east = False
            break
        y += 1
    if east:
        return True

    # check if visible from the West
    west = True
    y = c
    while y > 0:
        if trees[r][y - 1] >= height:
            west = False
            break
        y -= 1
    if west:
        return True


trees = []
for line in lines:
    trees.append([int(x) for x in list(line.strip())])

print(f"Trees: {trees}")
ROWS = len(trees)
COLS = len(trees[0])

visible_from_edge = ROWS * COLS - ((ROWS - 2) * (COLS - 2))
visible = 0
for row in range(1, ROWS - 1):
    for col in range(1, COLS - 1):
        if is_visible(row, col, trees, trees[row][col]):
            visible += 1
print(f"Part 1 answer, trees visible from outside of grid: {visible + visible_from_edge}")


