package main

import (
  "fmt"
  "net/http"
  "net/url"
  "os"
  "time"
  "io/ioutil"
)

func usage() {
  clue := []int{109,97,107,101,32,116,104,101,32,103,101,116,32,114,101,113,117,101,115,116,32,116,111,32,116,104,101,32,117,114,108,32,102,111,114,32,97,32,99,108,117,101,44,32,109,121,32,102,114,105,101,110,100}
  fmt.Println(clue)
}

func makeRequest(method, urlVal, headerKey, headerVal string) {
  client := &http.Client{
    Timeout: time.Second * 10,
  }

  req, err := http.NewRequest(method, urlVal, nil)
  req.Header.Add(headerKey, headerVal)

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    fmt.Println("Something went wrong with the request!")
    fmt.Println("This is probably not your fault...")
    fmt.Println("Please confirm the args you passed in are reachable!")
    fmt.Println("If they are not, please reach out to the organizers!")
    os.Exit(1)
  }

  body, err := ioutil.ReadAll(res.Body)
  fmt.Println(string(body))

  os.Exit(0)
}

func main() {
  if len(os.Args) != 5 {
    fmt.Println("If only the programmer had added help text...")
    os.Exit(1)
  }

  if os.Args[1] != "POST" && os.Args[1] != "GET" {
    fmt.Println("Invalid value in first argument")
    os.Exit(1)
  } else if os.Args[1] == "GET" {
    fmt.Println("Wrong one, dweeb!")
    os.Exit(1)
  }

  urlVal, err := url.Parse(os.Args[2])
  if err != nil {
    fmt.Println("Invalid value in second argument")
    os.Exit(1)
  }

  if urlVal.Scheme != "http" && urlVal.Scheme != "https" {
    fmt.Println("Nah, we don't need that type of request")
    os.Exit(1)
  } else if urlVal.Scheme == "https" {
    fmt.Println("Cmon, dog -- we don't have that kind of security...")
    os.Exit(1)
  }

  if urlVal.Host != "russian-bot.net:8000" {
    fmt.Println("You are looking in the wrong place")
    os.Exit(1)
  }

  if urlVal.Path != "/the_oogey_boogey_man" {
    fmt.Println("Dude... you aren't gonna guess this...")
    os.Exit(1)
  }

  fmt.Println("Alright... you passed my basic checks...")
  fmt.Println("Time to test your janky work...")
  fmt.Printf("\nMaking request with key of: %s\n", os.Args[3])
  fmt.Printf("Making request with value of: %s\n\n", os.Args[4])

  makeRequest(os.Args[1], os.Args[2], os.Args[3], os.Args[4])
  usage()
}
