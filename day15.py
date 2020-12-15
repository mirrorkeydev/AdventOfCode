import itertools
import re
import math
import copy

starter_numbers = [1,17,0,10,18,11,6]

spoken = {}

for i, number in enumerate(starter_numbers[:-1]):
    spoken[number] = i

last_number = starter_numbers[-1]
for i in range(len(starter_numbers), 30000000):
    new_number = 0
    if last_number in spoken:
        new_number = i - 1 - spoken[last_number]
    else:
        new_number = 0
    
    spoken[last_number] = i - 1
    last_number = new_number

print(last_number)
