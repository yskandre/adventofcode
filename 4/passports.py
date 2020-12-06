import re


def first():
    lines = open("4/pp.txt", "r").read().splitlines()

    count = 0
    criteria = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport = ""

    for line in lines:
        if line != "":
            passport += line + " "
        else:
            if all(x + ":" in passport for x in criteria):
                count += 1

            passport = ""

    if passport != "":
        if all(x + ":" in passport for x in criteria):
            count += 1

    print(count)


def second():
    lines = open("4/pp.txt", "r").read().splitlines()

    count = 0
    criteria = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport = ""

    for line in lines:
        if line != "":
            passport += line + " "
        else:
            if validate(passport, criteria):
                count += 1

            passport = ""

    if passport != "":
        if validate(passport, criteria):
            count += 1

    print(count)


def validate(passport: str, criteria):
    if all(x + ":" in passport for x in criteria):
        for data in passport.strip().split(" "):
            c, v = data.split(":")
            if "byr" == c:
                if not (v.isdigit() and len(v) == 4 and 1920 <= int(v) <= 2002):
                    return False
            if "iyr" == c:
                if not (v.isdigit() and len(v) == 4 and 2010 <= int(v) <= 2020):
                    return False
            if "eyr" == c:
                if not (v.isdigit() and len(v) == 4 and 2020 <= int(v) <= 2030):
                    return False
            if "hgt" == c:
                if "cm" == v[-2:]:
                    if not (150 <= int(v.strip("cm")) <= 193):
                        return False
                elif "in" == v[-2:]:
                    if not (59 <= int(v.strip("in")) <= 76):
                        return False
                else:
                    return False
            if "hcl" == c:
                if not re.match("#([0-9a-f]){6}", v):
                    return False
            if "ecl" == c:
                if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    return False
            if "pid" == c:
                if not (len(v) == 9 and v.isdigit()):
                    return False

        return True


if __name__ == "__main__":
    first()
    second()
