import itertools
import math

with open('input.txt', 'r') as f:
  input = [int(line.strip()) for line in f]

# Part A

sorted_input = sorted(input)
print(sorted_input)

num_1_difference = 0
num_3_difference = 0
for i, number in enumerate(sorted_input):
    if i == 0:
        if number == 1:
            num_1_difference += 1
        elif number == 3:
            num_3_difference += 1
    else:
        if number - sorted_input[i-1] == 1:
            num_1_difference += 1
        elif number - sorted_input[i-1] == 3:
            num_3_difference += 1

num_3_difference += 1

print(num_1_difference * num_3_difference)

# Part B

# sorted_aggregated_input = []
# for i, number in enumerate(sorted_input):
#     if i != 0 and number - sorted_input[i-1] == 3:
#         sorted_aggregated_input[-1] = (sorted_aggregated_input[-1][0], number)
#     else:
#         sorted_aggregated_input.append((number, number))

# print(sorted_aggregated_input)

# max_list = max(sorted_input)
# num_combinations = 0
# for i in range(len(sorted_aggregated_input), 0, -1):
#     print(i)
#     temp_num_combinations = 0
#     for combination in itertools.combinations(sorted_aggregated_input, r = i):
#         combination_good = True

#         if combination[-1][1] != max_list:
#             combination_good = False

#         for index, number in enumerate(combination):
#             if index == 0:
#                 if number[0] > 3:
#                     combination_good = False
#                     break
#             else:
#                 if number[0] - combination[index-1][1] > 3:
#                     combination_good = False
#                     break

#         if combination_good:
#             num_combinations += 1
#             temp_num_combinations += 1
    
#     if temp_num_combinations == 0:
#         break

adjacency_list = {}

root = 0
for j, possible_number in enumerate(sorted_input[:3]):
    if possible_number - root <= 3:
        if root in adjacency_list:
            adjacency_list[root].append(possible_number)
        else:
            adjacency_list[root] = [possible_number]

for i, number in enumerate(sorted_input):
    for j, possible_number in enumerate(sorted_input[i+1:i+4]):
        if possible_number - number <= 3:
            if number in adjacency_list:
                adjacency_list[number].append(possible_number)
            else:
                adjacency_list[number] = [possible_number]

adjacency_list[max(sorted_input)] = [max(sorted_input) + 3]

print(adjacency_list)
paths_counted = {}

def count_paths_down_route(number):
    number_possible_connections = 0
    if number == max(sorted_input) + 3:
        number_possible_connections = 1
    else:
        for possible_number in adjacency_list[number]:
            if possible_number in paths_counted:
                number_possible_connections += paths_counted[possible_number]
            else:
                result = count_paths_down_route(possible_number)
                number_possible_connections += result
                paths_counted[possible_number] = result

    return number_possible_connections

number_possible_connections = 0
for possible_number in adjacency_list[root]:
    number_possible_connections += count_paths_down_route(possible_number)

print(number_possible_connections)