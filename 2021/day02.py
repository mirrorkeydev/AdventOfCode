import re

f = open("input.txt", "r")
lines = f.readlines()

arr = []

for line in lines:
  arr.append(line)

position = 0
depth = 0
aim = 0

for val in arr:
  m = re.match(r"(\S+) (\d+)", val)
  command, num = m.groups()
  if command == "forward":
    position += int(num)
    depth += aim*int(num)
  elif command == "down":
    aim += int(num)
  elif command == "up":
    aim -= int(num)

print(position*depth)
