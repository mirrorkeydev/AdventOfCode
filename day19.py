import itertools
import re
import math
import copy

# Part A

with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]

with open('rules.txt', 'r') as f:
  rules = [line.strip() for line in f]

def evaluate_subsequence(string):
    split_value = string.split(" ")
    return_arr = []
    for number in split_value:
        if number in rules_char:
            return_arr.append(rules_char[number])
        else:
            result = evaluate_sequence(rules_nested[number])
            return_arr.append(result)
            rules_char[number] = result
    return "(?:" + "".join(return_arr) + ")"

def evaluate_sequence(string):
    if "|" in string:
        string_a, string_b = string.split("|")
        return "(?:" + evaluate_subsequence(string_a.strip()) + "|" + evaluate_subsequence(string_b.strip()) + ")"
    else:
        return evaluate_subsequence(string)

rules_nested = {}
rules_char = {}
for rule in rules:
    num, actual_rule = rule.split(":")
    actual_rule = actual_rule.strip()

    if actual_rule[0] == "\"":
        rules_char[num] = actual_rule[1]
    
    else:
        rules_nested[num] = actual_rule

thicc_regex = re.compile("^" + evaluate_sequence(rules_nested['0']) + "$")

count = 0
for line in input:
    if thicc_regex.match(line):
        count += 1

print(count)

# Part B

with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]

with open('rules.txt', 'r') as f:
  rules = [line.strip() for line in f]

def evaluate_subsequence(string):
    split_value = string.split(" ")
    return_arr = []
    for number in split_value:
        if number in rules_char:
            return_arr.append(rules_char[number])
        else:
            result = evaluate_sequence(rules_nested[number])
            return_arr.append(result)
            rules_char[number] = result
    return "(?:" + "".join(return_arr) + ")"

def evaluate_sequence(string):
    if "|" in string:
        string_a, string_b = string.split("|")
        return "(?:" + evaluate_subsequence(string_a.strip()) + "|" + evaluate_subsequence(string_b.strip()) + ")"
    else:
        return evaluate_subsequence(string)

rules_nested = {}
rules_char = {}
for rule in rules:
    num, actual_rule = rule.split(":")
    actual_rule = actual_rule.strip()

    if actual_rule[0] == "\"":
        rules_char[num] = actual_rule[1]
    
    else:
        rules_nested[num] = actual_rule

rules_char['8'] = evaluate_sequence(rules_nested['42']) + "+"

some_rule = []
for i in range(5):
    some_rule.append("(?:" + evaluate_sequence(rules_nested['42']) + "{" + str(i+1) + "}" + evaluate_sequence(rules_nested['31']) + "{" + str(i+1) + "})")

rules_char['11'] = "(?:" + "|".join(some_rule) + ")"

thicc_regex = re.compile("^" + evaluate_sequence(rules_nested['0']) + "$")

rule_42 = re.compile(evaluate_sequence(rules_nested['42']))
rule_31 = re.compile(evaluate_sequence(rules_nested['31']))

count = 0
for line in input:
    matches = thicc_regex.match(line)
    if matches:
        count += 1

print(count)
print(len("^" + evaluate_sequence(rules_nested['0']) + "$")) # -> 206470. oof
