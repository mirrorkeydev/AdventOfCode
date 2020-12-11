import copy

with open('input.txt', 'r') as f:
  input = [list(line.strip()) for line in f]

# Part A

def a(i, j, val, input):
    return 1 if (i >= 0 and i < len(input) and j >= 0 and j < len(input[0]) and input[i][j] == val) else 0

def count_adjacent_state(i,j, state, input):
    return (a(i-1,j-1, state, input) + a(i-1, j, state, input) + a(i-1, j+1, state, input) + a(i, j-1, state, input) + 
            a(i, j+1, state, input) + a(i+1, j-1, state, input) + a(i+1, j, state, input) + a(i+1, j+1, state, input))

# Part B

def in_bounds(i, j, input):
    return i >= 0 and i < len(input) and j >= 0 and j < len(input[0])

def ray_trace(i, j, istep, jstep, input, state):
    while in_bounds(i + istep, j + jstep, input):
        i += istep
        j += jstep

        if input[i][j] == state:
            return 1
        if input[i][j] == 'L' or input[i][j] == '#':
            return 0
    
    return 0

def count_visible_state(i,j, state, input):
    return (ray_trace(i, j, 1, 0, input, state) +
            ray_trace(i, j, 1, 1, input, state) +
            ray_trace(i, j, 0, 1, input, state) +
            ray_trace(i, j, -1, 1, input, state) +
            ray_trace(i, j, -1, 0, input, state) +
            ray_trace(i, j, -1, -1, input, state) +
            ray_trace(i, j, 0, -1, input, state) +
            ray_trace(i, j, 1, -1, input, state))

something_changed = True
while something_changed:
    something_changed = False
    copy_input = copy.deepcopy(input)

    for i, row in enumerate(copy_input):
        for j, thing in enumerate(row):

            if thing == "L" and count_visible_state(i,j, '#', input) == 0:
                copy_input[i][j] = '#'
                something_changed = True
            
            if thing == "#" and count_visible_state(i, j, "#", input) >= 5:
                copy_input[i][j] = 'L'
                something_changed = True
    
    input = copy_input

count = 0
for thing1 in input:
    for thing2 in thing1:
        if thing2 == "#":
            count += 1          

print(count)