import string

with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]
  input.append("")


groups = []
group = []
for line in input:
  if line == "":
    groups.append(group)
    group = []
  else:
    group.append(line)

big_count = 0

for group in groups:
  count = 0
  questions = list("abcdefghijklmnopqrstuvwxyz")
  occurences = {}
  num_in_group = len(group)

  for question in group:
    for question_char in question:
      if question_char in questions:
        if question_char in occurences:
          occurences[question_char] += 1
        else:
          occurences[question_char] = 1
    
  for question_char in occurences:
    if occurences[question_char] == num_in_group:
      count += 1
        
  big_count += count

print(big_count)