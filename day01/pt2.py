input = []
with open("input.txt") as file:
    for item in file.read().splitlines():
        input.append(int(item))

for num1 in input:
    for num2 in input:
        for num3 in input:
            if num1+num2+num3 == 2020:
                print(str(num1) + " + " + str(num2) +
                      " + " + str(num3) + "= 2020")
                print(str(num1) + " * " + str(num2) + " * " +
                      str(num3) + "= " + str(num1*num2*num3))
                exit()
