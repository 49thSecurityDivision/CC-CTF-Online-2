# Why?
More PWN

# What?
Hmm... Looks like we can't overwrite the instruction pointer...
nc 45.32.102.46 8005

# How Solve?
The code creates space on the heap for two tructs that basically just contain strings. It moves the values entered into two registers before they are moved to the address of the structs.
So, to solve, you have to find what registers are used and overwrite the first argument with the two addresses being used for the fields in the struct. Load them with the values of the 'cat' command and the 'flag.txt' address, and then the code will cat the flag.

# Flag
flag{SISimZUWJLwzf4iiHXgCfy5LmXgs6Ye-}
