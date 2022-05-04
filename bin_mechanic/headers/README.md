# Why?
Learn ELF, bro

# What? 
The important PT_LOAD header has been converted to PT_NOTE

# How Solve?
`readelf -l headers` reveals that there is a NOTE header that has executable permissions. This is also the largest header, which is extremely strange. Changing this to a PT_LOAD header by bit-flipping the start of the header from 04 to 01 will allow you to exec the binary.

# Challenge Description
Someone broke this binary too! 

Looks like this time they tampered with the program headers...

# Flag
flag{eutoi7AS9k9n0hKO7kpTNAnXtf6LxUXX}
