# Why?
Attempting to create a more real-world RE challenge

# What? 
Re-create a simplified version of the 1.0 HIVE ransomware. All details
on solving this challenge can be found in thid research paper:
https://arxiv.org/pdf/2202.08477.pdf

# How Solve?
The ransomware generated 10MB of random data and, for each file being
encrypted, grabs a 1KB stream from a pre-defined offset and uses that
to encrypt the filename AFTER adding the offset of the 1MB stream used
to actually XOR the file. 

So the encryption process looks like this:
1. Pass in a file to the malware
2. Malware picks from a pre-determined offset a 1KB stream
3. The filename is the appended with the offset of the 1MB stream used to encrypt the file
4. Then, the 1KB stream is used to encrypt the filename with a simple XOR
5. Then, the 1MB stream is used to encrypt the file with a simple XOR

# Flag
flag{H9EB04AAueg6LGVmHrmrKywynwe6zCMm}
