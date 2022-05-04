#!/usr/bin/python3
import random
import threading
import socket
import sys

default_board = '''... ... X..
... ..X ...
.X. ... ...

..X ... ...
... ... .X.
... X.. ...

... ... ..X
X.. ... ...
... .X. ...'''

count = 1

def test_uniq(nums):
  if len(nums) != 9:
    return False

  for i in range(1, 9):
    check = nums.find(str(i))
    if check == -1:
      print("didn't find {} in {}".format(i, nums))
      return False

  return True


def check(board, count):
  ind = 0
  boar_ind = 0
  row = 0
  col = 0
  sqr = 0

  # Basic smoke test (make sure the same answer isn't being passed in multiple times
  # This check only works if boards are generated using the Default Board variable
  # and not generating them randomly
  if (board[6] != str(count) or
    board[14] != str(count) or
    board[19] != str(count) or
    board[29] != str(count) or
    board[43] != str(count) or
    board[48] != str(count) or
    board[62] != str(count) or
    board[63] != str(count) or
    board[76] != str(count)
  ):
    print("This is not a correct solution for the given board")
    return False

  # Check the rows for 1-9 uniqueness
  while row < 9:
    test_row = board[ind:ind+9]

    if not test_uniq(test_row):
      return False

    row = row + 1
    ind = ind + 9

  print("Validated rows")
  ind = 0

  # Check the columns for 1-9 uniqueness
  while col < 9:
    test_col = ''.join([board[i] for i in [ind, ind+(9*1), ind+(9*2), ind+(9*3), ind+(9*4), ind+(9*5), ind+(9*6), ind+(9*7), ind+(9*8)]])

    if not test_uniq(test_col):
      return False

    col = col + 1
    ind = ind + 1
  
  print("Validated columns")
  ind = 0

  # check the appropriate 3x3 grids for 1-9 uniqueness
  while ind < 60:
    for first_loop in range(0, 3):
      grid = ''.join([board[i] for i in [ind, ind+1, ind+2, ind+9, ind+10, ind+11, ind+18, ind+19, ind+20]])
      if not test_uniq(grid):
        return False
      ind = ind + 3

    ind = ind + 18 # This should be 21, but because we add 3 at the end of the previous loop, we bumped in down
    if (ind+20) < len(board):
      grid = ''.join([board[i] for i in [ind, ind+1, ind+2, ind+9, ind+10, ind+11, ind+18, ind+19, ind+20]])
    if not test_uniq(grid):
      return False

  print("Validated grids")
  return True

while count <= 9:
  board = default_board
  board = board.split('\n')
  for line in range(0, len(board)):
    if "X" in board[line]:
      ind = board[line].index("X")
      board[line] = board[line][:ind] + str(count) + board[line][ind+1:]
  
  print("solve me quick:")
  board = input("\n".join(board) + "\n")
  print("Received something...")
  if not check(board, count):
    print("Hmm... That doesn't look right...")
    sys.exit()
  count = count + 1

if count == 9:
    print('flag{IEN3ZYcBSbAIYvp6TW8Jp3Sanv4O8tvp}')
sys.exit()
