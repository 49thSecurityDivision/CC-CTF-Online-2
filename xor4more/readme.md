## Example Name
by gen3, rated 2/5

## goal
Learn how rng affects xor, and what files look like. Hopefully learn `hexdump -C`

## prompt
A hacker has breached our system and left this file. See if you can decrypt it and see if you can find any leads.

## solution
Since the xor value repeats, you can deduce the value from part of the jpeg that are constant, like the magic number

## answer
flag{K9QLxjLYJCmyIIIfpOvdGgpuy7thWm56}