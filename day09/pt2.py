numbers = []

preamble = 25

with open("input.txt") as file:
    numbers = file.read().split("\n")

numbers = [int(x) for x in numbers]


def passes_number_check(number, previous):
    for num2 in previous:
        if number-num2 in previous:
            return True
    return False


for i, number in enumerate(numbers):
    if(i < preamble):
        continue

    past = numbers[i-preamble:i]
    if not passes_number_check(number, past):
        failed_num = number

for i, number in enumerate(numbers):
    current_try = 0
    index = 0
    while current_try < failed_num:
        current_try += numbers[i+index]
        index += 1
    if(current_try == failed_num):
        correct_numbers = numbers[i:i+index]
        correct_numbers.sort()
        print(correct_numbers[0]+correct_numbers[-1])
        break
