with open('day11-input.txt') as f:
    lines = f.readlines()


def operation(x: int, s: str, y: str):
    if s == '+':
        if y == 'old':
            return x + x
        else:
            return x + int(y)
    elif s == '*':
        if y == 'old':
            return x * x
        else:
            return x * int(y)


def is_divisible(x: int, y: int):
    return x % y == 0


monkeys = {}
for line in lines:
    note = line.strip()
    if note.startswith('Monkey'):
        num = note.split()[1].strip(':')
        monkeys[num] = {
            'items': [],
            'inspection_count': 0,
            'operation': {
                'symbol': None,
                'value': None,
                'func': None,
            },
            'test': {
                'predicate': None,
                'value': None,
                'true': None,
                'false': None,
            },
        }
    elif note.startswith('Starting'):
        items = note.split()[2:]
        monkeys[num]['items'] = [int(x.strip(',')) for x in items]
    elif note.startswith('Operation'):
        print(note.split())
        operands = note.split()[4:]
        symbol, value = operands[0], operands[1]
        monkeys[num]['operation']['symbol'] = symbol
        monkeys[num]['operation']['value'] = value
        monkeys[num]['operation']['func'] = lambda x, s, y: operation(x, s, y)
    elif note.startswith('Test'):
        y = note.split()[-1]
        monkeys[num]['test']['value'] = int(y)
        monkeys[num]['test']['predicate'] = lambda x, y: is_divisible(x, y)
    elif note.startswith('If true'):
        true = note.split()[-1]
        monkeys[num]['test']['true'] = true
    elif note.startswith('If false'):
        false = note.split()[-1]
        monkeys[num]['test']['false'] = false

print(monkeys)

# thanks to this thread for leading me to the idea
# https://www.reddit.com/r/adventofcode/comments/zih7gf/2022_day_11_part_2_what_does_it_mean_find_another/
# was pretty confused about how to progress here for a little bit
divisor = 1
for num in monkeys:
    divisor *= monkeys[num]['test']['value']

for r in range(10000):
    print(f"Round {r}!")
    for num in monkeys:
        print(f"Monkey {num}:")
        # inspect item
        for item in monkeys[num]['items']:
            print(f"  Monkey inspects an item with a worry level of {item}.")
            # get new worry level
            symbol = monkeys[num]['operation']['symbol']
            value = monkeys[num]['operation']['value']
            worry = monkeys[num]['operation']['func'](item, symbol, value)
            print(f"    New worry level is {worry}.")

            # divide worry level by 3, round down to nearest integer
            # worry //= 3
            worry = worry % divisor
            print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry}.")

            # check test
            y = monkeys[num]['test']['value']
            check = monkeys[num]['test']['predicate'](worry, y)

            # throw to monkey based on test result
            if check:
                m = monkeys[num]['test']['true']
                monkeys[m]['items'].append(worry)
            else:
                m = monkeys[num]['test']['false']
                monkeys[m]['items'].append(worry)
            print(f"    Item with worry level is thrown to monkey {m}.")

        # Add inspected items and empty the monkey's item list
        monkeys[num]['inspection_count'] += len(monkeys[num]['items'])
        monkeys[num]['items'] = []

inspected = []
for num in monkeys:
    print(f"Monkey {num} inspected {monkeys[num]['inspection_count']} items")
    inspected.append(monkeys[num]['inspection_count'])

inspected.sort(reverse=True)
print(f"Amount of monkey business: {inspected[0] * inspected[1]}")
