import re
with open('input.txt', 'r') as f:
    input = [line.strip() for line in f]
    input.append("")

passports = []
passport = ""
for line in input:
    if line == "":
        passports.append(passport)
        passport = ""
    else:
        passport += " " + line
        passport = passport.strip()

num_valid = 0
for passport in passports:
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    fields = passport.split(" ")
    for field in fields: 
        key, value = field.split(":")

        if key in required_keys:

            if key == "byr":
                value = int(value)
                if value < 1920 or value > 2002:
                    break

            if key == "iyr":
                value = int(value)
                if value < 2010 or value > 2020:
                    break

            if key == "eyr":
                value = int(value)
                if value < 2020 or value > 2030:
                    break
            
            if key == "hgt":
                match = re.match(r"^(\d{1,3})(cm|in)$", value)
                if match is None:
                    break
                num, unit = match.groups()
                if unit == "in":
                    num = int(num)
                    if num < 59 or num > 76:
                        break
                else:
                    num = int(num)
                    if num < 150 or num > 193:
                        break
            
            if key == "hcl":
                if not re.match(r"^#[0-9a-f]{6}$", value):
                    break
            
            if key == "ecl":
                if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    break

            if key == "pid":
                if not re.match(r"^[0-9]{9}$", value):
                    break
                
            required_keys.remove(key)

    if len(required_keys) == 0:
        num_valid += 1

print(num_valid)