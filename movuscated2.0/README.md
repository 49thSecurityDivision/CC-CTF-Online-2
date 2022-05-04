# Why?
RE challenge

# What?
Challenge shows how GCC (which movuscator is a wrapper for) identifies and stores strings in memory

# How Solve?
`rabin -s mov | grep flag`
Then grab address of global variable `flag0`
Then go to that address in r2 (or other decompiler) and view flag in little endian

# Flag
flag{KqU3tIdk5QUjosbolChwhE0YfEwUD9y3}
