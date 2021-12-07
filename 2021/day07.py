import re
import numpy as np
from collections import defaultdict

with open("input.txt") as f:
  arr = list((int(x.strip()) for x in f.readlines()[0].split(",")))

def get_cheapest_fuel(start, roi):
  cheapest_fuel = start
  for i in range(max(arr)):
    cur_fuel = 0
    for crab in arr:
      cur_fuel += roi(crab, i)
    if cur_fuel < cheapest_fuel:
      cheapest_fuel = cur_fuel
  return cheapest_fuel

# Part 1
print(get_cheapest_fuel(1000000, lambda c, i: abs(c - i)))
  
# Part 2
print(get_cheapest_fuel(1000000000, lambda c, i: int((abs(c - i)**2 + abs(c - i))/2)))
