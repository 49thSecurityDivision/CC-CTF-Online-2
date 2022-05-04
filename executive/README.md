# Why?
Much more annoying ROP challenge for the sadists

# What?
Call execv with two very specific args. It'll be fun, I promise.
nc 45.32.102.46 8002

# How Solve?
Find the padding needed to overwrite RIP.
Find ROP gadgets that pop RDI and RSI (both are needed to cal execv).
Find the address where the execv syscall is loaded into RAX.
Find the address of the strings required.
Add all to the ROP chain in the order required.
This can be demonstrated with -- ./executive < payload.txt

# Flag
flag{lTEdoVZpb05WBD7WPUlPkXakeWlbCeyw}
