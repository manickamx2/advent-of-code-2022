# https://stackoverflow.com/questions/20250396/converting-string-that-looks-like-a-list-into-a-real-list-python
# "Python comes with batteries included" :)
import ast

with open('day13-input.txt') as f:
    lines = f.readlines()


def compare(a, b):
    if a < b:
        return True
    elif a == b:
        return 'continue'
    else:
        return False


def compare_packets(left, right):
    print(f"Comparing packets {left} and {right}")
    if type(left) == int and type(right) == int:
        return compare(left, right)
    elif type(left) == list and type(right) == list:
        length = min(len(left), len(right))
        for idx in range(length):
            res = compare_packets(left[idx], right[idx])
            if res != 'continue':
                return res
        return compare(len(left), len(right))
    elif type(left) == int and type(right) == list:
        print(f"Mixed types, converting {left} to list and retrying")
        return compare_packets([left], right)
    elif type(left) == list and type(right) == int:
        print(f"Mixed types, converting {right} to list and retrying")
        return compare_packets(left, [right])


pair = 1
total = 0
for i in range(0, len(lines), 3):
    print(f"Pair {pair}:")
    group = []
    for line in lines[i:i+3]:
        group.append(line.strip())

    # make comparisons
    left, right = ast.literal_eval(group[0]), ast.literal_eval(group[1])
    print(
        f"Left: {left}\n"
        f"Right: {right}"
    )
    result = compare_packets(left, right)
    print(f"result: {result}\n")

    if result:
        total += pair

    pair += 1

# part 1
print(f"Part 1 answer: {total}")
