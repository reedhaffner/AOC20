requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
requirements.sort()

passports = []

valid_passports = 0


def validify_passport(pass_dict):
    try:

        # Birth Year
        if not (1920 <= int(pass_dict["byr"]) <= 2002):
            return False

        # Issue Year
        if not (2010 <= int(pass_dict["iyr"]) <= 2020):
            return False

        # Expiry Year
        if not (2020 <= int(pass_dict["eyr"]) <= 2030):
            return False

        # Height
        if (pass_dict["hgt"][-2:] == "cm"):
            if not (150 <= int(pass_dict["hgt"][:-2]) <= 193):
                return False
        elif (pass_dict["hgt"][-2:] == "in"):
            if not (59 <= int(pass_dict["hgt"][:-2]) <= 76):
                return False
        else:
            return False

        # Hair Color
        if not (pass_dict["hcl"][0] == "#"):
            return False

        if not (len(pass_dict["hcl"]) == 7):
            return False

        int(pass_dict["hcl"][1:], 16)

        # Eye Color
        if pass_dict["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        # Passport ID
        if not (len(pass_dict["pid"]) == 9):
            return False

        return True
    except:
        return False


with open("input.txt") as file:
    for passport in file.read().split("\n\n"):
        passport = passport.replace("\n", " ")
        passports.append(passport)

for passport in passports:
    values = passport.split(" ")

    pass_dict = {}

    for valind in values:
        try:
            key, value = valind.split(":")
        except:
            pass
        pass_dict[key] = value

    if(validify_passport(pass_dict)):
        valid_passports += 1

print(valid_passports)
