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
        print(number)
