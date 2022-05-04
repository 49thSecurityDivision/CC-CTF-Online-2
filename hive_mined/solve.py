#!/usr/bin/python3

def xor(s0, s1):
  xored = []
  for i in range(0, len(s0)):
    val = ord(s0[i]) ^ ord(s1[i])
    xored.append(format(val, '02x'))

  return xored

def main():
  print("Opening first file")
  with open("flag.txt", "r") as file:
    str0 = file.read()
  print("Got: " + str0)

  print("Opening second file")
  with open("flag.txt.hive", "r") as file:
    str1 = file.read()
  print("Got: " + str1)

  answer = xor(str0, str1)

  print(answer)

main()
