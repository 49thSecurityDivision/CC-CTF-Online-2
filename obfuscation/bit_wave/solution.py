#!/usr/bin/python3

with open('real.question', 'r') as file:
  b = file.read()

b = b.strip('\n')

f = bytearray(int(b[x:x+8], 2) for x in range(0, len(b), 8))

with open('output.test', 'wb') as file:
  file.write(f)
