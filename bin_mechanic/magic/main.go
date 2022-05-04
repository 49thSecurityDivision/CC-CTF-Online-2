package main

import (
  "fmt"
  "os"
)

func main() {
  flag0 := []byte{0x46, 0x4C, 0x61, 0x47, 0x7B, 0x55, 0x75, 0x75, 0x6F, 0x49, 0x37, 0x41, 0x53, 0x39, 0x6B, 0x39, 0x6E, 0x30, 0x65, 0x53, 0x6F, 0x37, 0x6C, 0x6c, 0x55, 0x4E, 0x41, 0x6E, 0x58, 0x74, 0x66, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  flag1 := []byte{0x66, 0x6D, 0x61, 0x67, 0x7B, 0x55, 0x75, 0x74, 0x6F, 0x49, 0x37, 0x41, 0x53, 0x39, 0x6B, 0x39, 0x6E, 0x30, 0x68, 0x4C, 0x6F, 0x37, 0x6B, 0x70, 0x54, 0x4E, 0x41, 0x6E, 0x58, 0x74, 0x66, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  flag2 := []byte{0x66, 0x6C, 0x61, 0x67, 0x7B, 0x55, 0x75, 0x74, 0x6F, 0x49, 0x37, 0x41, 0x53, 0x39, 0x6B, 0x39, 0x6E, 0x30, 0x68, 0x4B, 0x70, 0x37, 0x6B, 0x70, 0x54, 0x4E, 0x41, 0x6E, 0x58, 0x74, 0x66, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  flag3 := []byte{0x66, 0x6C, 0x61, 0x67, 0x7B, 0x55, 0x75, 0x74, 0x6F, 0x49, 0x37, 0x41, 0x53, 0x39, 0x6B, 0x39, 0x6E, 0x30, 0x68, 0x4B, 0x70, 0x37, 0x6B, 0x70, 0x54, 0x4E, 0x41, 0x6E, 0x58, 0x74, 0x66, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  flag4 := []byte{0x66, 0x6C, 0x61, 0x67, 0x7B, 0x55, 0x75, 0x74, 0x6F, 0x49, 0x37, 0x41, 0x53, 0x39, 0x6B, 0x3a, 0x6E, 0x30, 0x68, 0x4B, 0x6F, 0x37, 0x6B, 0x70, 0x54, 0x4E, 0x41, 0x6E, 0x58, 0x74, 0x66, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  flag5 := []byte{0x66, 0x6C, 0x61, 0x67, 0x7b, 0x63, 0x68, 0x77, 0x68, 0x4c, 0x3c, 0x44, 0x59, 0x41, 0x6b, 0x5e, 0x6E, 0x30, 0x68, 0x4B, 0x6F, 0x37, 0x6B, 0x70, 0x54, 0x4E, 0x41, 0x6E, 0x58, 0x74, 0x66, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  flag6 := []byte{0x66, 0x6C, 0x61, 0x67, 0x7B, 0x55, 0x75, 0x74, 0x6F, 0x49, 0x37, 0x41, 0x53, 0x3a, 0x6B, 0x39, 0x6E, 0x30, 0x68, 0x4B, 0x6F, 0x37, 0x6B, 0x70, 0x54, 0x4E, 0x41, 0x6E, 0x58, 0x74, 0x66, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  flag7 := []byte{0x66, 0x6C, 0x61, 0x67, 0x7B, 0x65, 0x75, 0x74, 0x6F, 0x69, 0x37, 0x41, 0x53, 0x39, 0x6B, 0x39, 0x6E, 0x30, 0x68, 0x4B, 0x4F, 0x37, 0x6B, 0x70, 0x54, 0x4E, 0x41, 0x6E, 0x58, 0x74, 0x66, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  flag8 := []byte{0x66, 0x6C, 0x61, 0x67, 0x7B, 0x55, 0x75, 0x74, 0x6F, 0x49, 0x37, 0x41, 0x53, 0x39, 0x6B, 0x39, 0x6E, 0x30, 0x68, 0x4B, 0x6F, 0x37, 0x6B, 0x70, 0x54, 0x4E, 0x42, 0x6E, 0x58, 0x74, 0x66, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  flag9 := []byte{0x66, 0x6C, 0x61, 0x67, 0x7B, 0x55, 0x75, 0x74, 0x6F, 0x49, 0x37, 0x41, 0x53, 0x39, 0x6B, 0x39, 0x6E, 0x30, 0x68, 0x4B, 0x6F, 0x37, 0x6B, 0x70, 0x54, 0x4E, 0x41, 0x6E, 0x58, 0x74, 0x67, 0x36, 0x4C, 0x78, 0x55, 0x58, 0x58, 0x7D}
  
  if flag0 == nil {
    fmt.Println("Something's wrong...")
  }
  if flag1 == nil {
    fmt.Println("Something's wrong...")
  }
  if flag2 == nil {
    fmt.Println("Something's wrong...")
  }
  if flag3 == nil {
    fmt.Println("Something's wrong...")
  }
  if flag4 == nil {
    fmt.Println("Something's wrong...")
  }
  if flag5 == nil {
    fmt.Println("Something's wrong...")
  }
  if flag6 == nil {
    fmt.Println("Something's wrong...")
  }
  if flag7 == nil {
    fmt.Println("Something's wrong...")
  }
  if flag8 == nil {
    fmt.Println("Something's wrong...")
  }
  if flag9 == nil {
    fmt.Println("Something's wrong...")
  }

  if len(os.Args) != 2 {
    fmt.Printf("Usage: %s [-c | -d]\n", os.Args[0])
    os.Exit(1)
  } else if os.Args[1] == "-c" {
    fmt.Println("Printing correct flag:")
    for ind, _ := range flag5 {
      fmt.Printf(string(flag5[ind]))
    }
    fmt.Printf("\n")
  } else if os.Args[1] == "-d" {
    fmt.Println("Printing incorrect flag:")
    for ind, _ := range flag7 {
      fmt.Printf(string(flag7[ind]))
    }
    fmt.Printf("\n")
  } else {
    fmt.Println("Printing random flag:")
    for ind, _ := range flag1 {
      fmt.Printf(string(flag1[ind]))
    }
    fmt.Printf("\n")
  }
}