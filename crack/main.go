package main

import (
  "fmt"
  "os"
)

func encrypt(str string) {
  key := []int{102,108,97,103,123,84,78,48,52,77,66,121,53,50,66,125}
  for k, i := range str {
    if i != ' ' {
      fmt.Printf("%c", rune(int(i) ^ key[k % len(key)]))
    } else {
      fmt.Printf(" ")
    }
  }
  fmt.Printf("\n")
}

func main() {
  if len(os.Args) != 2 {
    fmt.Printf("Usage: %s \"<string to encrypt>\"\n", os.Args[0])
    fmt.Printf("(string must be in quotes)\n")
  } else {
    encrypt(os.Args[1])
  }
}
