import itertools

with open("input.txt") as f:
  arr = list((x.split("|") for x in f.readlines()))
  
# Part 1

# # segments : true number
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

cfgs_indexes = {0: "abcefg", 1: "cf", 2: "acdeg", 3: "acdfg", 4: "bdcf", 5: "abdfg", 6: "abdefg", 7: "acf", 8: "abcdefg", 9: "abcdfg"}

# for line in arr:
#   candidates = {x: set() for x in "abcdefg"}
#   signal_patterns = line[0].strip().split()
#   output_vals = line[1].strip().split()
  
#   mapping = defaultdict(list)
#   for val in output_vals:
#     if len(val) in seg_num_to_num:
#       true_num = seg_num_to_num[len(val)]
#       for candidate_segment in configurations[true_num]:
#         for v in val:
#           candidates[candidate_segment].add(v)
#   break
          # 0123456
original = "abcdefg"
s = 0
for line in arr:
  signal_patterns = line[0].strip().split()
  # print(signal_patterns)
  output_vals = line[1].strip().split()
  one_pattern = [x for x in signal_patterns if len(x) == 2][0]
  four_pattern = [x for x in signal_patterns if len(x) == 4][0]
  seven_pattern = [x for x in signal_patterns if len(x) == 3][0]
  eight_pattern = [x for x in signal_patterns if len(x) == 7][0]
  c = 0
  remaining_perms = []
  for perm in itertools.permutations(original, len(original)):

    proposed_one_pattern = "".join([perm[i] for i in range(len(original)) if original[i] in configurations[1]])
    if sorted(proposed_one_pattern) != sorted(one_pattern):
      continue
    
    proposed_four_pattern = "".join([perm[i] for i in range(len(original)) if original[i] in configurations[4]])
    if sorted(proposed_four_pattern) != sorted(four_pattern):
      continue

    proposed_seven_pattern = "".join([perm[i] for i in range(len(original)) if original[i] in configurations[7]])
    if sorted(proposed_seven_pattern) != sorted(seven_pattern):
      continue
    
    proposed_eight_pattern = "".join([perm[i] for i in range(len(original)) if original[i] in configurations[8]])
    if sorted(proposed_eight_pattern) != sorted(eight_pattern):
      continue
        
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
  # print(final_perm)
      
  if len(final_perm) != 1:
    raise Exception

  fp = final_perm[0]

  nums = []
  for ov in output_vals:
    converted_pattern = "".join([original[i] for i in range(len(original)) if fp[i] in ov])
    # print(ov, "->", converted_pattern)
    if converted_pattern not in configurations_reversed:
      raise Exception
    nums.append(configurations_reversed["".join(sorted(converted_pattern))])
  
  s += int("".join([str(x) for x in nums]))

print(s)
