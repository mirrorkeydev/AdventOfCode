import math

with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]

directions = ["N", "E", "S", "W"]

way_pos = [10, 1]
cur_pos = [0, 0]
cur_facing = 1

def move_direction(instruction, argument, cur_pos):
    if instruction == "S":
        cur_pos[1] -= argument

    elif instruction == "E":
        cur_pos[0] += argument

    elif instruction == "W":
        cur_pos[0] -= argument

    elif instruction == "N":
        cur_pos[1] += argument

for line in input:
    instruction = line[0]
    argument = int(line[1:])

    if instruction in ["S", "E", "W", "N"]:
        move_direction(instruction, argument, way_pos)
    
    elif instruction in ["L", "R"]:
        if instruction == "L":
            dist_vector = way_pos
            change = int(argument/90)
            while change:
                change -= 1
                dist_vector = [-dist_vector[1], dist_vector[0]]
            
            way_pos = dist_vector
        
        elif instruction == "R":
            dist_vector = way_pos
            change = int(argument/90)
            while change:
                change -= 1
                dist_vector = [dist_vector[1], -dist_vector[0]]
            
            way_pos = dist_vector
    
    elif instruction in ["F"]:
        cur_pos = [cur_pos[0] + way_pos[0]*argument, cur_pos[1] + way_pos[1]*argument]

print(abs(cur_pos[0]) + abs(cur_pos[1]))