# Why?
Learn ELF, bro

# What? 
Beginning of a series of challenges that involve repairing ELF files to get them to run

# How Solve?
Technically, the problem can be solved by RE, but that would be extremely difficult. The real way to solve it is to examine the ELF header and recognize that its filetype and exec format have been tampered with.
The filetype should be 02 (executable) and its exec format should be 3E (ELF). 
These can be edited with hexedit or really any other way.

# Challenge Description
Someone has tampered with this ELF file so it can no longer run.

This is supposed to be an executable x86_64 ELF. It needs some fixing before it can properly run.

# Flag
flag{UutoI7AS9k9n0hKo7kpTNAnXtf6LxUXX}
