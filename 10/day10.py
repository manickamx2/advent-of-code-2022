with open('day10-input.txt') as f:
    lines = f.readlines()

x = 1
cycles = 1
register = {cycles: x}
for line in lines:
    instruction = line.strip().split()
    print(f"instruction: {instruction}")
    cycles += 1
    register[cycles] = x
    print(f"cycle: {cycles} | x: {x}")
    if instruction[0] == 'addx':
        cycles += 1
        x += int(instruction[1])
        register[cycles] = x
        print(f"cycle: {cycles} | x: {x}")

signal_strength = 0
for i in range(20, 260, 40):
    print(f"i: {i}, register[{i}]: {register[i]}")
    signal_strength += i * register[i]

# part 1
print(f"Signal strength: {signal_strength}")
