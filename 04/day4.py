########## PART 1 ##########

with open('day4-input.txt') as f:
    lines = f.readlines()


def is_fully_contained(intervals):
    interval_one, interval_two = intervals[0], intervals[1]
    s1, e1 = interval_one.split('-')
    s2, e2 = interval_two.split('-')

    if (int(s1) <= int(e2) <= int(e1) and int(s1) <= int(s2) <= int(e1)) or \
            (int(s2) <= int(s1) <= int(e2) and int(s2) <= int(e1) <= int(e2)):
        return True


total = 0
for line in lines:
    if is_fully_contained(line.strip().split(',')):
        total += 1

print(f"part 1 answer: {total}")


def is_overlapping(intervals):
    interval_one, interval_two = intervals[0], intervals[1]
    s1, e1 = interval_one.split('-')
    s2, e2 = interval_two.split('-')

    if (int(s1) <= int(s2) <= int(e1)) or (int(s2) <= int(s1) <= int(e2)):
        return True


total = 0
for line in lines:
    if is_overlapping(line.strip().split(',')):
        total += 1

print(f"part 2 answer: {total}")
