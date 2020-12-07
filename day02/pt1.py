import re

valid = 0

match = "([\d]+)-([\d]+) ([\w]): ([\w]+)"

with open("input.txt") as file:
    for item in file.read().splitlines():
        pmin, pmax, pletter, password = re.match(match, item).groups()
        pmin, pmax = int(pmin), int(pmax)
        if pmin <= password.count(pletter) <= pmax:
            valid += 1

print(str(valid))
