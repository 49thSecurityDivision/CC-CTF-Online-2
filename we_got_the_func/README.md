# Why?
Veeeeeery basic ROP challenge. Good to keep the spirits high.

# What? 
Call a function that is not called from any direct code path.
nc 45.32.102.46 8001

# How Solve?
Grab the function address from nm, or r2, or anything really.
Find the padding needed to overwrite RIP.
Overwrite RIP with the function address.
(payload.txt in this repo will solve the challenge -- ./we_got_the_func < payload.txt)

# Flag
flag{XZT58Qlb5D-1Ux7b2nz1DPe76cAhsgvo}
