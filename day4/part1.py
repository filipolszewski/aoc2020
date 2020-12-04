import re


def get_passport_dict(passport):
    return {entry.split(":")[0]: entry.split(":")[1] for entry in passport.replace("\n", " ").split(" ")}


def is_valid_part_one(passport):
    return all(x in passport.keys() for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def validate_number(value, low, high):
    try:
        number = int(value)
        return low <= number <= high
    except ValueError:
        return False


def validate_height(param):
    if param.endswith("cm"):
        return validate_number(param[:-2], 150, 193)
    if param.endswith("in"):
        return validate_number(param[:-2], 59, 76)
    return False


def validate_hair_color(color):
    if re.match("^#[a-f0-9]{6}$", color):
        return True
    else:
        return False


def validate_id(pass_id):
    if re.match("^[0-9]{9}$", pass_id):
        return True
    else:
        return False


def validate_eye_color(color):
    return color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_part_two(passport):
    if not is_valid_part_one(passport):
        return False

    return (validate_number(passport.get("byr"), 1920, 2002)
            and validate_number(passport.get("iyr"), 2010, 2020)
            and validate_number(passport.get("eyr"), 2020, 2030) and validate_height(
        passport.get("hgt")) and validate_hair_color(passport.get("hcl")) and validate_eye_color(passport.get("ecl")) and validate_id(passport.get("pid")))


with open("input.txt", 'r') as data:
    passports = [get_passport_dict(passport) for passport in data.read().split("\n\n")]

result_one = sum([is_valid_part_one(passport) for passport in passports])
print(result_one)

result_two = sum([is_valid_part_two(passport) for passport in passports])
print(result_two)
