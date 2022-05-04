import re


pos = lambda x: ord(x) % 32
calc = lambda x, y: [i + j for i, j in zip(x, y)]
wrap = lambda x: [i % 27 for i in x]
ksi = lambda x: [pos(i) for i in x]

hint = 'By the pricking of my thumbs, Something wicked this way comes.'

print('Key 1 hint: Name of the play the phrase is from.')
print('Key 2 hint: Name of the author of the play.')
print('Key 3 hint: Son of the author of the play.')

print()

plaintext = 'FriendsRomanscountrymenlendmeyourearsIcometoburyCaesarnottopraisehimTheevilthatmendolivesafterthemThegoodisoftinterredwiththeirbones'
plaintext = re.sub("\W", '', plaintext)

plaintext_len = len(plaintext)

# Convert plaintext to integers
plaintext_int = []
for c in plaintext:
    plaintext_int.append(pos(c))

# Keystream 1
keystream_1 = 'Macbeth'
keystream_1_len = len(keystream_1)
print('Keystream 1:', keystream_1, keystream_1_len)
keystream_1_padded = (plaintext_len // keystream_1_len) * keystream_1 \
                     + keystream_1[:plaintext_len % keystream_1_len]

# Convert keystream to int
keystream_1_int = ksi(keystream_1_padded)
print('KSI 1:', keystream_1_int)

# Wrap keystream 0 - 25
ciphertext_1_int = calc(plaintext_int, keystream_1_int)
print('Ciphertext 1:', ciphertext_1_int)

# Wrap numbers to 0 - 25
wrapped_ciphertext_1 = wrap(ciphertext_1_int)
print('Wrapped Ciphertext 1:', wrapped_ciphertext_1)

print()

# Keystream 2
keystream_2 = 'WilliamShakespeare'
keystream_2_len = len(keystream_2)
print('Keystream 2:', keystream_2, keystream_2_len)
keystream_2_padded = (plaintext_len // keystream_2_len) * keystream_2 \
                     + keystream_2[:plaintext_len % keystream_2_len]

# Convert keystream to int
keystream_2_int = ksi(keystream_2_padded)
print('KSI 2:', keystream_2_int)

# Wrap keystream 0 - 25
ciphertext_2_int = calc(wrapped_ciphertext_1, keystream_2_int)
print('Ciphertext 2:', ciphertext_2_int)

# Wrap numbers to 0 - 25
wrapped_ciphertext_2 = wrap(ciphertext_2_int)
print('Wrapped Ciphertext 2:', wrapped_ciphertext_2)

print()

# Keystream 3
keystream_3 = 'HamnetShakespeare'
keystream_3_len = len(keystream_3)
print('Keystream 3:', keystream_3, keystream_3_len)
keystream_3_padded = (plaintext_len // keystream_3_len) * keystream_3 \
                     + keystream_3[:plaintext_len % keystream_3_len]

# Convert keystream to int
keystream_3_int = ksi(keystream_3_padded)
print('KSI 3:', keystream_3_int)

# Wrap keystream 0 - 25
ciphertext_3_int = calc(wrapped_ciphertext_2, keystream_3_int)
print('Ciphertext 3:', ciphertext_3_int)

# Wrap numbers to 0 - 25
wrapped_ciphertext_3 = wrap(ciphertext_3_int)
print('Wrapped Ciphertext 3:', wrapped_ciphertext_3)

print()

ciphertext = ''.join([chr(x + 96) for x in wrapped_ciphertext_3])
print('Triple Stream Ciphertext:', ciphertext)
print()
print(plaintext)
