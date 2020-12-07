p_right = 3
p_down = 1

c_pos_x = 0

value = 0

with open("input.txt") as file:
    x_lines = file.read().splitlines()

length = len(x_lines) - p_down

for line in range(0, length, p_down):
    x_line = x_lines[line+p_down]
    if (c_pos_x < len(x_line)-p_right):
        c_pos_x += p_right
    else:
        c_pos_x = c_pos_x-len(x_line)+p_right
    if x_line[c_pos_x] == "#":
        value += 1

print(value)
