import itertools

with open("input.txt") as f:
  arr = list((x.split("|") for x in f.readlines()))
  
# Part 1

seg_num_to_num = {2: 1, 4: 4, 3: 7, 7: 8}

count = 0
for line in arr:
  signal_patterns = line[0].strip().split()
  output_vals = line[1].strip().split()
  
  for val in output_vals:
    if len(val) in seg_num_to_num:
      count += 1

print(count)

# Part 2

configurations = {0: "abcefg", 1: "cf", 2: "acdeg", 3: "acdfg", 4: "bcdf", 5: "abdfg", 6: "abdefg", 7: "acf", 8: "abcdefg", 9: "abcdfg"}
configurations_reversed = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}

original = "abcdefg"
s = 0
for line in arr:
  signal_patterns = line[0].strip().split()
  output_vals = line[1].strip().split()

  patterns = [[x for x in signal_patterns if len(x) == i][0] for i in [2, 4, 3, 7]]
  remaining_perms = []
  for perm in itertools.permutations(original, len(original)):
    invalid = False
    proposed_patterns = ["".join([perm[i] for i in range(len(original)) if original[i] in configurations[j]]) for j in [1, 4, 7, 8]]

    for i in range(len(patterns)):
      if sorted(patterns[i]) != sorted(proposed_patterns[i]):
        invalid = True
        break
        
    if not invalid:
      remaining_perms.append("".join(perm))

  final_perm = []
  for perm in remaining_perms:
    valid = True
    for sp in signal_patterns:
      converted_pattern = "".join([original[i] for i in range(len(original)) if perm[i] in sp])
      if converted_pattern not in configurations_reversed:
        valid = False
    if valid:
      final_perm.append(perm)
      
  if len(final_perm) != 1:
    raise Exception

  fp = final_perm[0]

  nums = []
  for ov in output_vals:
    converted_pattern = "".join([original[i] for i in range(len(original)) if fp[i] in ov])
    if converted_pattern not in configurations_reversed:
      raise Exception
    nums.append(configurations_reversed["".join(sorted(converted_pattern))])
  
  s += int("".join([str(x) for x in nums]))

print(s)
