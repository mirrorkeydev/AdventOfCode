import copy

with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]

instructions = []
for line in input:
    instruction, number = line.split(" ")
    if number[0] == "+":
        number = int(number[1:])
    else:
        number = 0 - int(number[1:])
    instructions.append([instruction, number])

print(instructions)

for i, thing in enumerate(instructions):

    instuctions_copy = copy.deepcopy(instructions)
    if thing[0] == 'jmp':
        instuctions_copy[i][0] = 'nop'
    elif thing[0] == 'nop':
        instuctions_copy[i][0] = 'jmp'
    else:
        continue

    counter = 0
    accumulator = 0
    visited_instructions = {}

    while counter not in visited_instructions and counter < len(instructions):
        visited_instructions[counter] = True

        instruction, number = instuctions_copy[counter]
        if instruction == 'acc':
            accumulator += number
            counter += 1
        elif instruction == 'nop':
            counter += 1
        elif instruction == 'jmp':
            counter += number
    
    if counter == len(instructions):
        print('found')
        break

print(accumulator)