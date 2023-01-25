import math
import re

with open('day15-input.txt') as f:
    lines = f.readlines()


def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return int(abs(x1 - x2) + abs(y1 - y2))


def mark_positions(d, sensor, grid, no_beacons):
    sx, sy = sensor
    for dy in range(-d, d + 1):
        y = sy + dy
        if y not in no_beacons:
            no_beacons[y] = []
        for dx in range(-d, d + 1):
            x = sx + dx
            if manhattan_distance((x, y), sensor) > d:
                continue
            else:
                if (x, y) not in grid:
                    coordinate = Coordinate(x, y)
                    coordinate.marked = True
                    grid[(x, y)] = coordinate
                    no_beacons[y].append('#')


def print_grid(grid, min_x, max_x, min_y, max_y):
    start = min(min_x, min_y)
    for y in range(start, max_y + 1):
        print(y, end=' ')
        for x in range(start, max_x + 1):
            c = grid.get((x, y))
            if c:
                print(str(c), end='')
            else:
                print('.', end='')
        print()


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.marked = False

    def __str__(self):
        return '.' if not self.marked else '#'


class Sensor(Coordinate):
    def __init__(self, x, y, beacon):
        super().__init__(x, y)
        self.closest_beacon = beacon

    def __str__(self):
        return 'S'


class Beacon(Coordinate):

    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return 'B'


min_x, min_y = math.inf, math.inf
max_x, max_y = 0, 0
matcher = re.compile(r'Sensor at x=([^.]+), y=([^.]+): closest beacon is at x=([^.]+), y=([^.]+)')
grid = {}
no_beacons = {}
for line in lines:
    info = line.strip()
    result = matcher.match(info)
    if result:
        coordinate_values = [int(x) for x in result.groups()]
        sx, sy, bx, by = coordinate_values

        closest_beacon = Beacon(bx, by)
        sensor = Sensor(sx, sy, closest_beacon)
        grid[(sx, sy)] = sensor
        grid[(bx, by)] = closest_beacon

        d = manhattan_distance((sx, sy), (bx, by))
        mark_positions(d, (sx, sy), grid, no_beacons)

        min_x = min(sx, bx, min_x)
        max_x = max(sx, bx, max_x)

        min_y = min(sy, by, min_y)
        max_y = max(sy, by, max_y)

target = 2000000
print(len(no_beacons[target]))
