lines = []

with open("input.txt") as file:
    f = file.read().split("\n")
    for line in f:
        lines.append([line[:3], int(line[4:]), False])


pointer = 0
value = 0
loop_tripped = False

while not loop_tripped:
    instruction, val, tripped = lines[pointer]
    if tripped:
        loop_tripped = True
        break
    if(instruction == "nop"):
        lines[pointer] = [instruction, val, True]
        pointer += 1
    if(instruction == "acc"):
        lines[pointer] = [instruction, val, True]
        value += val
        pointer += 1
    if(instruction == "jmp"):
        lines[pointer] = [instruction, val, True]
        pointer += val

print(value)
