with open('input.txt', 'r') as f:
    input = [line.strip() for line in f]

num_trees1 = 0
for i in range(1, len(input)):
    if input[i][i % len(input[i])] == "#":
        num_trees1 += 1

num_trees2 = 0
for i in range(1, len(input)):
    if input[i][(i*3) % len(input[i])] == "#":
        num_trees2 += 1

num_trees3 = 0
for i in range(1, len(input)):
    if input[i][(i*5) % len(input[i])] == "#":
        num_trees3 += 1

num_trees4 = 0
for i in range(1, len(input)):
    if input[i][(i*7) % len(input[i])] == "#":
        num_trees4 += 1

num_trees5 = 0
index = 1
for i in range(2, len(input), 2):
    if input[i][index % len(input[i])] == "#":
        num_trees5 += 1
    index += 1

print(num_trees1 * num_trees2 * num_trees3 * num_trees4 * num_trees5)