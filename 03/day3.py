########## PART 1 ##########

with open('day3-input.txt') as f:
    lines = f.readlines()


def find_common_in_rucksack(line):
    compartment_one = set(line[:len(line) // 2])
    compartment_two = set(line[len(line) // 2:])

    return compartment_one & compartment_two


def get_priority(item):
    val = ord(item)
    if val >= ord('a'):
        return val - ord('a') + 1
    else:
        return val - ord('A') + 27


total_priorities = 0
for line in lines:
    common_item = find_common_in_rucksack(line.strip()).pop()
    priority = get_priority(common_item)
    total_priorities += priority

print(f"part 1 answer: {total_priorities}")

########## PART 2 ##########

def find_common_in_group(group):
    compartment_one, compartment_two, compartment_three = set(group[0]), set(group[1]), set(group[2])

    return compartment_one & compartment_two & compartment_three


group = []
total_priorities = 0
for line in lines:
    group.append(line.strip())
    if len(group) < 3:
        continue
    else:
        print(f"group: {group}")
        common_item = find_common_in_group(group).pop()
        print(f"common item: {common_item}")
        priority = get_priority(common_item)
        total_priorities += priority
        group = []

print(f"part 2 answer: {total_priorities}")
