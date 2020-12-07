input = []
with open("input.txt") as file:
    for item in file.read().splitlines():
        input.append(int(item))

for num1 in input:
    for num2 in input:
        if num1+num2 == 2020:
            print(str(num1) + " + " + str(num2) + "= 2020")
            print(str(num1) + " * " + str(num2) + "= " + str(num1*num2))
            exit()
