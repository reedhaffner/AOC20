requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
requirements.sort()

passports = []

valid_passports = 0

with open("input.txt") as file:
    for passport in file.read().split("\n\n"):
        passport = passport.replace("\n", " ")
        passports.append(passport)

for passport in passports:
    values = passport.split(" ")

    keys = []

    for valind in values:
        try:
            key, value = valind.split(":")
        except:
            pass
        keys.append(key)

    if "cid" in keys:
        keys.remove("cid")

    keys.sort()

    if keys == requirements:
        valid_passports += 1

print(valid_passports)
