# Why?
"Scripting" challenge for nerds. The sudoku Z3 solver python code is available online, so maybe easy?

# What?
Solve 9 consecutive sudoku challenges using Z3.

# How Solve?
Use the provided Z3 solver script (which can be found online) to solve all 9 challenges.
This should take no longer than 4 minutes, but if network lag is an issue, we can allocate
8 minutes.

# Challenge Description
Solve a series of challenges sudoku boards.

The boards are presented in this format:
.34 6.. .12
6.. ... ...
.9. 3.2 ...

.5. 7.1 4.3
... ..3 .9.
7.. .2. ...

.6. ... .84
... .1. ...
3.5 2.. 1..

And, the accepted answers are a single string of numbers representing the solved board starting from the top left and ending in the bottom right. 

For example, if this is the solved board:
534 678 912
672 195 348
198 342 567

859 761 423
426 853 791
713 924 856

961 537 284
287 419 635
345 286 179

Then you would submit:
534678912672195348198342567859761423426853791713924856961537284287419635345286179

nc 45.32.102.46 8004

# Flag
flag{W-PBfLQAdgSLg3xm7IPwtOPr54jbdOeW}
