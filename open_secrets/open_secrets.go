package main

import (
  "os"
  "fmt"
)

func main() {
  if len(os.Args) != 3 {
    fmt.Printf("%s <first secret> <second secret>\n", os.Args[0])
    return
  }

  if os.Args[1] == "admin" && os.Args[2] == "administrator" {
    fmt.Println("flag{K4Xqn4qXZFJyVW4MvKIX5Sg5jW1RJecm}")
    return
  }

  if os.Args[1] == "administrator" && os.Args[2] == "admin" {
    fmt.Println("flag{K4Xqn4qXZFJyVW4MvKIX5Sg5jW1RJecm}")
    return
  }

  fmt.Println("Hmmm... Seems wrong to me...")
}
