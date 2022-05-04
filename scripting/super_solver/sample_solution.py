#!/usr/bin/env python3

import itertools
import sys
import z3
import socket
from enum import Enum
from pwn import *

class SudokuType(Enum):
    Classic = 1

class Sudoku:

    _grid = [[ None for _ in range(9) ] for _ in range(9) ]
    _solver = None
    _valid_charset = set([str(x) for x in range(1,10)])
    sudoku_type = SudokuType.Classic

    _nums = [[ '.' for _ in range(9) ] for _ in range(9) ]
    _extra_constraints = []
    
    def __init__(self, sudoku_string=""):
        self._solver = z3.Solver()
        sudoku_string = "".join(sudoku_string)
        self._valid_charset.add('.')

        # Create variables
        for r in range(9):
            for c in range(9):
                v = z3.Int('cell_%d_%d' % (r+1, c+1))
                self._grid[r][c] = v

        # Add constraints for classic sudoku
        self.add_classic_constraints()

        assert (len(sudoku_string) >= 81), "Invalid sudoku string provided! (length)"
        self.load_numbers(sudoku_string[:81])

    def load_numbers(self, sudoku_string):
            for r in range(9):
                for c in range(9):
                    x = sudoku_string[r*9+c]
                    assert (x in self._valid_charset), "Invalid sudoku string provided! (invalid character \'{}\')".format(x)
                    if(x != '.'):
                        self._nums[r][c] = int(x)
                        self._solver.add(self._grid[r][c] == int(x))

    def print(self):
        for r in range(9):
            print('   '
                    .join(["{} {} {}".format(a,b,c) for a,b,c in 
                        zip(self._nums[r][::3], self._nums[r][1::3], self._nums[r][2::3])]))
            if(r in [2, 5]):
                print()

    def raw_print(self):
        board = ""
        for r in range(9):
            board +=(''.join(["{}{}{}".format(a,b,c) for a,b,c in 
                        zip(self._nums[r][::3], self._nums[r][1::3], self._nums[r][2::3])]))
        return board

    def get_offset_constraints(self, offsets, symmetrical):
        pairs = set()
        for r in range(9):
            for c in range(9):
                for dy,dx in offsets:
                    y = r+dy
                    x = c+dx
                    if not ((0 <= x <= 8) and (0 <= y <= 8)):
                        continue
                    pair = tuple(sorted([(r,c), (y,x)]))
                    if symmetrical and (pair in pairs):
                        continue
                    pairs.add(pair)
                    yield self._grid[r][c], self._grid[y][x]

    def add_classic_constraints(self):
        # Digits from 1-9
        for r in range(9):
            for c in range(9):
                v = self._grid[r][c]
                self._solver.add(v >= 1)
                self._solver.add(v <= 9)

        # Distinct digits in row/column
        for i in range(9):
            self._solver.add(z3.Distinct(self._grid[i])) # Row
            self._solver.add(z3.Distinct([self._grid[r][i] for r in range(9)])) # Column

        # Distinct digits in boxes
        offset = list(itertools.product(range(0,3), range(0,3)))
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = [self._grid[r+dy][c+dx] for dy,dx in offset]
                self._solver.add(z3.Distinct(box))

    def solve(self):
        if self._solver.check() == z3.sat:
            m = self._solver.model()
            for r in range(9):
                for c in range(9):
                    self._nums[r][c] = m.evaluate(self._grid[r][c])
            return True
        else:
            return False

if __name__ == "__main__":
  soc = remote('45.32.102.46', '8004')

  for i in range(0, 9):
    # get past intro banner
    data = ""
    while data != "s":
      data = soc.recv(1).decode()
    data += soc.recv(14).decode()
    print(data)
    soc.recv(1).decode()
    board = soc.recv(110).decode()
    print("Printing challenge:")
    print(board)
    board = "".join(board.split())

    s = Sudoku(board)

    print("Entered sudoku:")
    print(s.sudoku_type)
    print()

    if(s.solve()):
        print("Solved sudoku")
        board = s.raw_print()
        soc.send(board.encode())
        soc.send("\n".encode())
    else:
        soc.close()
        print("Too many constraints? -- cannot solve")
