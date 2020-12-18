with open('input.txt', 'r') as f:
  input = [int(line.strip()) for line in f]

current_25 = []
goal = 0
# Part A
for i, line in enumerate(input):
    if i < 25:
        current_25.append(line)
    else:
        found = False
        for num in current_25:
            goal = line
            if goal-num in current_25:
                found = True
                break
        
        if not found:
            goal = line
            print(line)
            break

        current_25.pop(0)
        current_25.append(line)

# Part B
running_sum = 0
sums = []
for i, line in enumerate(input):
    running_sum += line
    sums.append(running_sum)

found_range = []
for i, sum1 in enumerate(sums):
    for j, sum2 in enumerate(sums[:i]):
        if sum1-sum2 == goal and i - j >= 2:
            found_range = [j, i]
            break

j = found_range[0]
i = found_range[1]

print(min(input[j:i+1]) + max(input[j:i+1]))