from collections import defaultdict

with open("input.txt") as f:
  fishies = list((int(x.strip()) for x in f.readlines()[0].split(",")))

# Part 1:

for i in range(80):
  new_fishies = []
  for j in range(len(fishies)):
    if fishies[j] == 0:
      fishies[j] = 6
      new_fishies.append(8)
    else:
      fishies[j] = fishies[j] - 1
  fishies += new_fishies

print(len(fishies))

# Part 2:

with open("input.txt") as f:
  fishies = list((int(x.strip()) for x in f.readlines()[0].split(",")))

num_each_timer = defaultdict(lambda: 0)

for fish in fishies:
  num_each_timer[fish] += 1

for i in range(256):
  num_each_timer_new = defaultdict(lambda: 0)
  for j in range(8, -1, -1):
    if j == 0:
      num_each_timer_new[8] += num_each_timer[j] if j in num_each_timer else 0
      num_each_timer_new[6] += num_each_timer[j] if j in num_each_timer else 0
    else:
      num_each_timer_new[j-1] = num_each_timer[j] if j in num_each_timer else 0
  num_each_timer = num_each_timer_new

print(sum([key for _, key in num_each_timer.items()]))
