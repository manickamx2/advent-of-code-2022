import heapq
with open('day12-input.txt') as f:
    lines = f.readlines()


def climb_hill(start, end, heights):
    visited = set()
    visited.add(start)
    cells = []
    path_distance = 0
    while start != end:
        r, c = start
        current_elevation = heights[start]
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            # check to see if new coordinate is valid
            if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS:
                continue
            difference = current_elevation - heights.get((new_r, new_c), float('inf'))
            if (new_r, new_c) not in visited and difference >= -1:
                visited.add((new_r, new_c))
                heapq.heappush(cells, (difference, path_distance + 1, (new_r, new_c)))
        if not cells:
            return float('inf')
        _, path_distance, start = heapq.heappop(cells)
    return path_distance


directions = [
    [0, 1],   # right
    [1, 0],   # down
    [0, -1],  # left
    [-1, 0]   # up
]

# get S and E locations
starts = []
heights = {}
ROWS, COLS = 0, 0
for row, line in enumerate(lines):
    ROWS += 1
    for col, char in enumerate(line.strip()):
        COLS += 1
        if char == 'S':
            print(f"Start position 'S' coordinates: {row, col}")
            start = (row, col)
            starts.append(start)
            value = 0
        elif char == 'E':
            print(f"End position 'E' coordinates: {row, col}")
            end = (row, col)
            value = 26
        else:
            value = ord(char) - ord('a') + 1
        heights[(row, col)] = value

print(climb_hill(start, end, heights))
