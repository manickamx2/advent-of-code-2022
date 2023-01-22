with open('day14-input.txt') as f:
    lines = f.readlines()


def fill_grid(grid, y_max, x_max):
    for y in range(y_max + 1):
        for x in range(490, x_max + 1):
            if (x, y) not in grid:
                grid[(x, y)] = Cell(x, y, 'air')
    return grid


def print_grid(grid, y_max, x_max):
    for y in range(y_max + 1):
        for x in range(490, x_max + 1):
            cell = grid.get((x, y))
            if cell:
                print(str(cell), end='')
            else:
                print('.', end='')
        print()


def fill_gaps(prev):
    prev_x, prev_y = prev
    # horizontal gaps
    if x > prev_x:
        for i in range(prev_x + 1, x + 1):
            grid[(i, y)] = Cell(i, y, 'rock')
    elif prev_x > x:
        for i in range(x + 1, prev_x + 1):
            grid[(i, y)] = Cell(i, y, 'rock')
    # vertical gaps
    if y > prev_y:
        for i in range(prev_y + 1, y + 1):
            grid[(x, i)] = Cell(x, i, 'rock')
    elif prev_y > y:
        for i in range(x + 1, prev_x + 1):
            grid[(x, i)] = Cell(x, i, 'rock')


def calculate_next_position(gx, gy):
    # down, down-left, down-right
    directions = [(0, 1), (-1, 1), (1, 1)]
    for dx, dy in directions:
        x = gx + dx
        y = gy + dy
        cell = grid.get((x, y), None)

        if not cell:
            # we have reached the void
            return x, y, False, True
        if cell.type == 'air':
            # we can reach this position, return
            return x, y, False, False

    # blocked in all directions
    return gx, gy, True, False


class Cell:

    def __init__(self, row, col, type):
        self.row = row
        self.col = col
        self.type = type

    def __str__(self):
        if self.type == 'rock':
            return '#'
        elif self.type == 'sand':
            return 'o'
        elif self.type == 'source':
            return '+'
        elif self.type == 'air':
            return '.'


grid = {}
x_max, y_max = 0, 0
for line in lines:
    rocks = line.strip().split(' -> ')
    prev = None
    for r in rocks:
        coordinate = r.split(',')
        x, y = int(coordinate[0]), int(coordinate[1])

        if prev:  # fill gaps
            fill_gaps(prev)
        x_max = max(x, x_max)
        y_max = max(y, y_max)
        cell = Cell(x, y, 'rock')
        grid[(x, y)] = cell
        prev = (x, y)

# sand source is (500, 0)
source = (500, 0)
grid[source] = Cell(500, 0, 'source')
grid = fill_grid(grid, y_max, x_max)

print_grid(grid, y_max, x_max)
print("-"*100)

# simulate sand falling
sand_can_fall = True
grains_of_sand = 0
while sand_can_fall:
    # sand can fall, initialize a grain of sand
    gx, gy = source
    at_rest = False
    while not at_rest:
        gx, gy, blocked, endless_void = calculate_next_position(gx, gy)

        if endless_void:
            print((gx, gy))
            sand_can_fall = False
            at_rest = True

        if blocked:
            # update the grid
            grid[(gx, gy)].type = 'sand'
            at_rest = True
            grains_of_sand += 1
    print_grid(grid, y_max, x_max)
    print("-"*100)

print(f"Part 1 answer: {grains_of_sand}")
