########## PART 1 ##########
import math

RIGHT = 'R'
UP = 'U'
LEFT = 'L'
DOWN = 'D'

with open('day9-input.txt') as f:
    lines = f.readlines()


def compute_distance(p1: tuple, p2: tuple):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


# initialize a 'visited' set
visited = set()

# H and T both start at (0, 0)
hx, hy = 0, 0
tx, ty = 0, 0
visited.add((0, 0))

for line in lines:
    move = line.strip().split()
    direction, units = move[0], int(move[1])

    if direction == RIGHT:
        x = 0
        while x < units:
            x += 1
            hx += 1
            distance = compute_distance((hx, hy), (tx, ty))
            if distance > math.sqrt(2):  # head and tail are not touching, need to move tail to keep up
                if tx != hx and ty != hy:  # head and tail are in different rows and columns
                    # move tail directly next to head
                    tx, ty = hx - 1, hy
                else:
                    tx += 1
            visited.add((tx, ty))
    elif direction == UP:
        y = 0
        while y < units:
            y += 1
            hy += 1
            distance = compute_distance((hx, hy), (tx, ty))
            if distance > math.sqrt(2):  # head and tail are not touching, need to move tail to keep up
                if tx != hx and ty != hy:  # head and tail are in different rows and columns
                    # move tail directly next to head
                    tx, ty = hx, hy - 1
                else:
                    ty += 1
            visited.add((tx, ty))
    elif direction == LEFT:
        x = 0
        while x < units:
            x += 1
            hx -= 1
            distance = compute_distance((hx, hy), (tx, ty))
            if distance > math.sqrt(2):  # head and tail are not touching, need to move tail to keep up
                if tx != hx and ty != hy:  # head and tail are in different rows and columns
                    # move tail directly next to head
                    tx, ty = hx + 1, hy
                else:
                    tx -= 1
            visited.add((tx, ty))
    elif direction == DOWN:
        y = 0
        while y < units:
            y += 1
            hy -= 1
            distance = compute_distance((hx, hy), (tx, ty))
            if distance > math.sqrt(2):  # head and tail are not touching, need to move tail to keep up
                if tx != hx and ty != hy:  # head and tail are in different rows and columns
                    # move tail directly next to head
                    tx, ty = hx, hy + 1
                else:
                    ty -= 1
            visited.add((tx, ty))

# part 1
print(f"Number of positions that the tail of the rope visited at least once: {len(visited)}")