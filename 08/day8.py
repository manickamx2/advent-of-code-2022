########## PART 1 ##########
from typing import List

with open('day8-input.txt') as f:
    lines = f.readlines()


def compute_scenic_score(r: int, c: int, trees: List, height: int):

    # get North multiplier
    x = r
    while x > 0:
        x -= 1
        if trees[x][c] >= height:
            break
    north_multiplier = r - x

    # get South multiplier
    x = r
    while x < ROWS - 1:
        x += 1
        if trees[x][c] >= height:
            break
    south_multiplier = x - r

    # get East multiplier
    y = c
    while y < COLS - 1:
        y += 1
        if trees[r][y] >= height:
            break
    east_multiplier = y - c

    # get West multiplier
    y = c
    while y > 0:
        y -= 1
        if trees[r][y] >= height:
            break
    west_multiplier = c - y

    return north_multiplier * south_multiplier * east_multiplier * west_multiplier


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
scenic_scores = []
for row in range(1, ROWS - 1):
    for col in range(1, COLS - 1):
        if is_visible(row, col, trees, trees[row][col]):
            visible += 1
        score = compute_scenic_score(row, col, trees, trees[row][col])
        scenic_scores.append(score)

print(f"Part 1 answer, trees visible from outside of grid: {visible + visible_from_edge}")
print(f"Part 2 answer, maximum scenic score: {max(scenic_scores)}")
