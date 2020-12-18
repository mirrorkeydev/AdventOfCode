with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]

rule_set = {}

for line in input:
  words = line.split("contain")
  bag = words[0].replace(".", "").replace("bags", "").replace("bag", "").strip()
  can_contain = words[1:]
  for rule_list in can_contain:
    rules = rule_list.split(",")
    for rule in rules:
      cleaned_rule = rule.replace(".", "").replace("bags", "").replace("bag", "").strip()
      
      if "no other" in cleaned_rule:
        continue

      number, *other_bag = cleaned_rule.split(" ")
      other_bag = " ".join(other_bag)
      if bag in rule_set:
        rule_set[bag].append([int(number), other_bag])
      else:
        rule_set[bag] = [[int(number), other_bag]]

# Part A
num_bags = 0
bags_to_check = ["shiny gold"]
bags_already_validated = {}
while len(bags_to_check):
  new_bags_to_check = []
  for bag in rule_set:
    for bag_to_check in bags_to_check:
      for bag2 in rule_set[bag]:
        bag3 = bag2[1]
        if bag_to_check == bag3 and bag not in bags_already_validated:
          num_bags += 1
          new_bags_to_check.append(bag)
          bags_already_validated[bag] = True
  bags_to_check = new_bags_to_check
print(num_bags)

# Part B
num_bags_inside_gold_bag = 0
bags_to_check = ["shiny gold"]
while len(bags_to_check):
  bag_to_check = bags_to_check.pop(0)
  if bag_to_check in rule_set:
    ls = rule_set[bag_to_check]
    for nested_bag in ls:
      num_bags_inside_gold_bag += nested_bag[0]
      for i in range(nested_bag[0]):
        bags_to_check.append(nested_bag[1])

print(num_bags_inside_gold_bag)