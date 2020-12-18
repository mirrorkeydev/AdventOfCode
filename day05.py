import math

with open('input.txt', 'r') as f:
    input = [line.strip() for line in f]


seat_ids = []
for ticket in input:
    row = ticket[:7]

    top = 127
    bottom = 0

    for direction in row:
        if direction == "F":
            top = math.floor(top - (top-bottom)/2)
        else:
            bottom = math.ceil(bottom + (top-bottom)/2)
    
    row = top

    left = 0
    right = 7
    
    col = ticket[7:]
    for direction in col:
        if direction == "L":
            right = math.floor(right - (right - left)/2)
        else:
            left = math.ceil(left + (right - left)/2)

    seat_id = row * 8 + left

    seat_ids.append(seat_id)

p = sorted(seat_ids)
for i, seat in enumerate(p):
    if abs(seat - p[i+1]) == 2:
        print(seat + 1)

    
            