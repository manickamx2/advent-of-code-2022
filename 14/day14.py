import math

with open('day14-input.txt') as f:
    lines = f.readlines()


def fill_grid(grid, y_max, x_max, x_min):
    for y in range(y_max):
        for x in range(x_min, x_max):
            if (x, y) not in grid:
                grid[(x, y)] = Cell(x, y, 'air')
    return grid


def print_grid(grid, y_max, x_max, x_min):
    for y in range(y_max):
        for x in range(x_min, x_max):
            cell = grid.get((x, y))
            if cell:
                print(str(cell), end='')
            else:
                print('.', end='')
        print()


def calculate_next_position(sand):
    # down, down-left, down-right
    gx, gy = sand
    directions = [(0, 1), (-1, 1), (1, 1)]
    for dx, dy in directions:
        x = gx + dx
        y = gy + dy
        cell = grid.get((x, y), None)

        if not cell:
            # we have reached the void
            return None, None
        elif cell.type != 'rock' and cell.type != 'sand':
            # we can reach this position, return
            return x, y

    # blocked in all directions
    return gx, gy


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
x_min = math.inf
x_max, y_max = 0, 0
for line in lines:
    rocks = line.strip().split(' -> ')
    start = rocks[0].split(',')
    start_x, start_y = int(start[0]), int(start[1])
    for r in range(1, len(rocks)):
        coordinates = rocks[r].split(',')
        end_x, end_y = int(coordinates[0]), int(coordinates[1])

        while start_x != end_x:
            x_max = max(start_x, x_max)
            x_min = min(start_x, x_min)
            grid[(start_x, start_y)] = Cell(start_x, start_y, 'rock')
            if start_x > end_x:
                start_x -= 1
            else:
                start_x += 1

        while start_y != end_y:
            y_max = max(start_y, end_y, y_max)
            grid[(start_x, start_y)] = Cell(start_x, start_y, 'rock')
            if start_y > end_y:
                start_y -= 1
            else:
                start_y += 1

        x_max = max(start_x, end_x, x_max)
        y_max = max(start_y, end_y, y_max)

        grid[(end_x, end_y)] = Cell(end_x, end_y, 'rock')
        start_x, start_y = end_x, end_y

# sand source is (500, 0)
source = (500, 0)
grid[source] = Cell(500, 0, 'source')
grid = fill_grid(grid, y_max, x_max, x_min)

# simulate sand falling
sand_can_fall = True
grains_of_sand = 0
while sand_can_fall:
    # sand can fall, initialize a grain of sand
    sand = source
    at_rest = False
    while not at_rest:
        nx, ny = calculate_next_position(sand)

        if (nx, ny) == (None, None):
            sand_can_fall = False
            at_rest = True
        elif (nx, ny) == sand:
            # update the grid
            grid[(nx, ny)].type = 'sand'
            grains_of_sand += 1
            at_rest = True

        sand = (nx, ny)

print(f"Part 1 answer: {grains_of_sand}")