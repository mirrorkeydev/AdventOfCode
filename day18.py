import itertools
import re
import math
import copy

# with open('input.txt', 'r') as f:
#   input = [line.strip() for line in f]

# def recurse_group(string):
#     total = 0
#     index = 0
#     pre_group_operator = '+'
#     while index < len(string):
#         if string[index] == "(":
#             sub_total, offset = recurse_group(string[index + 1:])
#             index += offset + 2
#             if pre_group_operator == "+":
#                 total += sub_total
#             else:
#                 total *= sub_total
#             continue

#         elif string[index] == ")":
#             return (total, index)
        
#         elif re.match(r"\d", string[index]):
#             if pre_group_operator == "+":
#                 total += int(string[index])
#             else:
#                 total *= int(string[index])
        
#         elif re.match(r"[+*]", string[index]):
#             pre_group_operator = string[index]

#         index += 1
        
#     return (total, index)

# my_sum = 0
# for line in input:
#     line = line.replace(" ", "")
#     total, offset = recurse_group(line)

#     my_sum += total

# print(my_sum)

with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]

def reverse_pemdas(string):
    equations_with_plusses = string.split("*")
    sub_totals = []
    for equation in equations_with_plusses:
        sub_total = 0
        stuff_to_add = equation.split("+")
        for number in stuff_to_add:
            number = int(number)
            sub_total += number
        sub_totals.append(str(sub_total))

    return "*".join(sub_totals)

def multiply_string_culm(multiply_string):
    total = 1
    if '*' not in multiply_string:
        return int(multiply_string)
    for num in multiply_string.split('*'):
        total *= int(num)
    return total

def regex_paren_away(string):
    while True:
        PAREN_REGEX = r"\(([*+\d]+)\)"
        matches = re.finditer(PAREN_REGEX, string)
        count = 0
        for match in matches:
            multiply_string = reverse_pemdas(match.group(1))
            total = multiply_string_culm(multiply_string)
            string = string.replace(f"({match.group(1)})", str(total))
            count += 1
        if not count:
            break
    return multiply_string_culm(reverse_pemdas(string))


my_sum = 0
for line in input:
    line = line.replace(" ", "")
    total = regex_paren_away(line)

    my_sum += total

print(my_sum)