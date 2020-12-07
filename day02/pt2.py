import re

valid = 0

match = "([\d]+)-([\d]+) ([\w]): ([\w]+)"

with open("input.txt") as file:
    for item in file.read().splitlines():
        pmin, pmax, pletter, password = re.match(match, item).groups()
        pmin, pmax = int(pmin)-1, int(pmax)-1
        if(password[pmin] == pletter) ^ (password[pmax] == pletter):
            valid += 1

print(str(valid))
