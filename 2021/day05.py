import re
import numpy as np

with open("input.txt") as f:
  arr = list((x.strip() for x in f.readlines()))

# Part 1:

lines = []
for row in arr:
  m = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", row)
  if not m:
    raise Exception
  x1, y1, x2, y2 = m.groups()
  lines.append((int(x1), int(y1), int(x2), int(y2)))

max_size = max([max(x) for x in [row for row in lines]])
board = np.zeros((max_size + 1, max_size + 1), dtype=int)

for line in lines:
  x1, y1, x2, y2 = line
  if x1 == x2:
    for i in range(y1, y2 - (1 if y1 > y2 else (-1)), -1 if y1 > y2 else 1):
      board[i][x1] = board[i][x1] + 1
  
  if y1 == y2:
    for i in range(x1, x2 - (1 if x1 > x2 else (-1)), -1 if x1 > x2 else 1):
      board[y1][i] = board[y1][i] + 1

print((board >= 2).sum())

# Part 2
for line in lines:
  x1, y1, x2, y2 = line
  if x1 == x2:
    continue # we already did this in part 1

  elif y1 == y2:
    continue # and this as well

  else: # draw a diagonal
    cur_x, cur_y = x1, y1
    while cur_x != x2 and cur_y != y2:
      board[cur_y][cur_x] = board[cur_y][cur_x] + 1
      cur_x = cur_x + (1 if x2 > x1 else -1)
      cur_y = cur_y + (1 if y2 > y1 else -1)
    board[cur_y][cur_x] = board[cur_y][cur_x] + 1

print((board >= 2).sum())
