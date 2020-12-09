original_lines = []

with open("input.txt") as file:
    f = file.read().split("\n")
    for line in f:
        original_lines.append([line[:3], int(line[4:]), False])

possible_fixes = [original_lines]

for line_changed in range(len(original_lines)):
    new_fix = original_lines[:line_changed]
    line_to_possibly_change = original_lines[line_changed]
    if(line_to_possibly_change[0] == "nop"):
        new_fix.append(["jmp", line_to_possibly_change[1], False])
        new_fix.extend(original_lines[line_changed+1:])
    elif(line_to_possibly_change[0] == "jmp"):
        new_fix.append(["nop", line_to_possibly_change[1], False])
        new_fix.extend(original_lines[line_changed + 1:])
    else:
        continue
    possible_fixes.append(new_fix)


pointer = 0
value = 0
loop_tripped = False

for iteration in range(len(possible_fixes)):
    lines_to_do = possible_fixes[iteration]
    pointer = 0
    value = 0
    loop_tripped = False

    while not loop_tripped:
        if(pointer >= len(lines_to_do)):
            print(value)
            break
        instruction, val, tripped = lines_to_do[pointer]
        if tripped:
            loop_tripped = True
            break
        if(instruction == "nop"):
            lines_to_do[pointer] = [instruction, val, True]
            pointer += 1
        if(instruction == "acc"):
            lines_to_do[pointer] = [instruction, val, True]
            value += val
            pointer += 1
        if(instruction == "jmp"):
            lines_to_do[pointer] = [instruction, val, True]
            pointer += val
