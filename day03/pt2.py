import math

p_pos = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

c_pos_x = 0

values = []

with open("input.txt") as file:
    x_lines = file.read().splitlines()

for pos in p_pos:

    p_right = pos[0]
    p_down = pos[1]

    length = len(x_lines) - p_down

    value = 0

    for line in range(0, length, p_down):
        x_line = x_lines[line+p_down]
        if (c_pos_x < len(x_line)-p_right):
            c_pos_x += p_right
        else:
            c_pos_x = c_pos_x-len(x_line)+p_right
        if x_line[c_pos_x] == "#":
            value += 1

    values.append(value)
    c_pos_x = 0

print(math.prod(values))
