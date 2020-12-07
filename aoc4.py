import re

def get_input():
    with open('input4.txt') as file:
        return [x.strip() for x in file]

def get_passports():
    lines = get_input()
    if lines[-1] != "":
        lines.append("")
    result = []
    for line in lines:
        if line == "":
            yield dict(result)
            result = []
        else:
            result.extend([x.split(":") for x in line.split(" ")])


required_fields = [
    "byr", # (Birth Year)
    "iyr", # (Issue Year)
    "eyr", # (Expiration Year)
    "hgt", # (Height)
    "hcl", # (Hair Color)
    "ecl", # (Eye Color)
    "pid", # (Passport ID)
#    "cid" # (Country ID)
]

def is_valid(passport):
    return set(passport.keys()).issuperset(required_fields)

valid_passports = filter(is_valid, get_passports())

print(len(list(valid_passports)))


def has_valid_byr(passport):
    byr = int(passport["byr"])
    return 1920 <= byr and byr <= 2002

def has_valid_iyr(passport):
    iyr = int(passport["iyr"])
    return 2010 <= iyr and iyr <= 2020

def has_valid_eyr(passport):
    eyr = int(passport["eyr"])
    return 2020 <= eyr and eyr <= 2030

def has_valid_hgt(passport):
    m = re.match("^(\\d{2,3})(cm|in)$", passport["hgt"], re.MULTILINE)
    if m:
        height, unit = m.groups()
        height = int(height)
        if unit=="cm":
            return 150 <= height and height <= 193
        else:
            return 59 <= height and height <= 76
    else:
        return False

def has_valid_hcl(passport):
    return re.match("^#[0-9a-f]{6}$",passport["hcl"], re.MULTILINE) is not None

def has_valid_ecl(passport):
    return passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def has_valid_pid(passport):
    return re.match("^\\d{9}$", passport["pid"], re.MULTILINE) is not None

def is_really_valid(passport):
    return (is_valid(passport) and 
        has_valid_byr(passport) and
        has_valid_iyr(passport) and
        has_valid_eyr(passport) and
        has_valid_hgt(passport) and
        has_valid_hcl(passport) and
        has_valid_ecl(passport) and
        has_valid_pid(passport))


p = {
    "eyr":"2029",
    "cid":"100",
    "hcl":"#a97842",
    "ecl":"blu",
    "hgt":"150cm",
    "pid":"8960565391",
    "iyr":"2014",
    "byr":"1989" }
print(has_valid_pid(p))


really_valid_passports = filter(is_really_valid, get_passports())
print(len(list(really_valid_passports)))