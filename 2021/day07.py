with open("input.txt") as f:
  arr = list((int(x.strip()) for x in f.readlines()[0].split(",")))

def get_cheapest_fuel(delta):
  cheapest_fuel = 1000000000
  for i in range(max(arr)):
    cur_fuel = 0
    for crab in arr:
      cur_fuel += delta(crab, i)
    if cur_fuel < cheapest_fuel:
      cheapest_fuel = cur_fuel
  return cheapest_fuel

# Part 1
print(get_cheapest_fuel(lambda c, i: abs(c - i)))
  
# Part 2
# Formula for nth triangular number (n^2+n)/2 from here: https://math.stackexchange.com/q/60578
print(get_cheapest_fuel(lambda c, i: int((abs(c - i)**2 + abs(c - i))/2)))
