########## PART 1 ##########

with open('day1-input.txt') as f:
    lines = f.readlines()

calories = 0
elf_calories = []
for line in lines:
    if line == '\n':
        elf_calories.append(calories)
        calories = 0
        continue
    calories += int(line.strip())

elf_calories.sort()
print(elf_calories[-1])

########## PART 2 ##########
print(sum(elf_calories[-3:]))