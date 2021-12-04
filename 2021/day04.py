import re
import sys

# with open("input.txt") as f:
#   #arr = list(map(int, (x.strip() for x in f.readlines())))
#   arr = list((x.strip() for x in f.readlines()))

f = open("input.txt", "r")
lines = f.readlines()
arr = []
for line in lines:
  arr.append(line.strip())

print(arr)

numbers_to_draw = [x for x in arr[0].split(",")]

boards = []
board = []
for row in arr[2:]:
  if row == '':
    boards.append(board)
    board = []
    continue
  m = re.match(r"(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", row)
  if m == None:
    raise Exception
  board.append([*m.groups()])
boards.append(board)

for board in boards:
  for row in board:
    print(row)
  print("")

def check_if_winner(board, drawn_numbers) -> bool:
  for row in board:
    winner_horizontal = True
    for val in row:
      if val not in drawn_numbers:
        winner_horizontal = False
    if winner_horizontal:
      return True
  
  # transposed
  for row in [[row[i] for row in board] for i in range(len(board[0]))]:
    winner_vertical = True
    for val in row:
      if val not in drawn_numbers:
        winner_vertical = False
    if winner_vertical:
      return True
  
  return False

drawn_numbers = []
for num in numbers_to_draw:
  drawn_numbers.append(num)
  for board in boards:
    is_winner = check_if_winner(board, drawn_numbers)
    if is_winner:
      print("winner:", board)
      winning_board = board
      unmarked_nums_sum = 0
      for row in winning_board:
        for val in row:
          if val not in drawn_numbers:
            unmarked_nums_sum += int(val)
      print(unmarked_nums_sum*int(num))
      boards = [x for x in boards if x is not winning_board]

