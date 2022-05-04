# Triple Stream
- triple_stream.txt
  - Challenge file with ciphertext
- triple_stream_cipher.py
  - Python script used to encrypt message
- triple_stream_solution.py
  - Python script to solve the challenge

## Why?
I spent too much time on this for some reason.
More fun math using stream cipher!

## How to Solve?
Start by finding the keys:
- Name of the play the phrase is from: Macbeth
- Name of the author of the play: WilliamShakespeare
- Name of the Son of the author of the play: HamnetShakespeare

# Challenge Description
By the pricking of my thumbs, Something wicked this way comes.

Keys in order used to encrypt message:
- Key 1 hint: Name of the play the phrase is from.
- Key 2 hint: Name of the author of the play.
- Key 3 hint: Son of the author of the play.

Flag: flag{<first lastname of message's speaker>}

Do NOT include spaces in keys and flag!

# Flog
flag{MarcAntony}
