########## PART 1 ##########

with open('day2-input.txt') as f:
    lines = f.readlines()

strategies = {
    'A': {
        'X': 3 + 1,
        'Y': 6 + 2,
        'Z': 0 + 3,
    },
    'B': {
        'X': 0 + 1,
        'Y': 3 + 2,
        'Z': 6 + 3,
    },
    'C': {
        'X': 6 + 1,
        'Y': 0 + 2,
        'Z': 3 + 3,
    },
}


def calculate_result(strategies: dict, match: str):
    # Opponent's moves      My moves
    # A -> Rock             # X -> Rock (1 point)
    # B -> Paper            # Y -> Paper (2 points)
    # C -> Scissors         # Z -> Scissors (3 points)
    moves = [x.strip() for x in match.split(' ')]
    theirs, ours = moves[0], moves[1]
    points = strategies.get(theirs).get(ours)
    return points


total_points = 0
for line in lines:
    points = calculate_result(strategies, line)
    total_points += points

print(f"part 1 answer: {total_points}")

########## PART 2 ##########
pt2_strategies = {
    'A': {
        'X': 0 + 3,
        'Y': 3 + 1,
        'Z': 6 + 2,
    },
    'B': {
        'X': 0 + 1,
        'Y': 3 + 2,
        'Z': 6 + 3,
    },
    'C': {
        'X': 0 + 2,
        'Y': 3 + 3,
        'Z': 6 + 1,
    },
}
total_points = 0
for line in lines:
    points = calculate_result(pt2_strategies, line)
    total_points += points

print(f"part 2 answer: {total_points}")
