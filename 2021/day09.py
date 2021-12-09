import math

with open("input.txt") as f:
  arr = list([int(y) for y in x.strip()] for x in f.readlines())

# Part 1
def is_lower(x, y, board):
  cur = board[y][x]
  if y > 0 and board[y - 1][x] <= cur:
    return False
  elif y < len(board) - 1 and board[y + 1][x] <= cur:
    return False
  elif x > 0 and board[y][x - 1] <= cur:
    return False
  elif x < len(board[0]) - 1 and board[y][x + 1] <= cur:
    return False

  return True

s = 0
low_locations = []
for y_val in range(len(arr)):
  for x_val in range(len(arr[0])):
    if is_lower(x_val, y_val, arr):
      s += arr[y_val][x_val] + 1
      low_locations.append((x_val, y_val))

print(s)

# Part 2
def walk_basin(board, marked, x, y):
  if x < 0 or y < 0 or x > len(board[0]) - 1 or y > len(board) - 1:
    return 0

  if (x, y) in marked or board[y][x] == 9:
    return 0 
  
  marked.add((x, y))

  s = 0
  for x_off, y_off in ((1, 0), (-1, 0), (0, -1), (0, 1)):
    s += walk_basin(board, marked, x + x_off, y + y_off)

  return s + 1

marked = set()
sizes = []
for loc in low_locations:
  x, y = loc
  sizes.append(walk_basin(arr, marked, x, y))

print(math.prod(sorted(sizes)[-3:]))
