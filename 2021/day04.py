import re

f = open("input.txt", "r")
lines = f.readlines()
arr = []
for line in lines:
  arr.append(line.strip())

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

def is_winner(board, drawn_numbers) -> bool:
  def winner(board, drawn_numbers):
    for row in board:
      winner = True
      for val in row:
        if val not in drawn_numbers:
          winner = False
      if winner:
        return True
  horizontal = winner(board, drawn_numbers)
  vertical = winner([[row[i] for row in board] for i in range(len(board[0]))], drawn_numbers)
  return True if horizontal or vertical else False

for i in range(len(numbers_to_draw)):
  for board in boards:
    if is_winner(board, numbers_to_draw[:i+1]):
      unmarked_nums_sum = 0
      for row in board:
        for val in row:
          if val not in numbers_to_draw[:i+1]:
            unmarked_nums_sum += int(val)
      print(unmarked_nums_sum*int(numbers_to_draw[i]))
      # Part 1: sys.exit(0) here
      boards = [b for b in boards if b is not board]

