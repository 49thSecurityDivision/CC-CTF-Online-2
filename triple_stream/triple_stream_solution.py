

# ciphertext = 'wbjffredyasptegnmhtmthqhalp`utomsdhjbhvygvtsrpwadupdvnqjkyhttrqvvqulzrvyzmufzzl`dyisvgdubdcgzgoscbskjstycjppwoortzwqspthnmnsinhm nfkbrulnntrmarvhjpzvrjghnvlgkhhoymakynhcyrgpfjtpamzmv`jsevivzthaheopxdnemk`gdpsuagdprswenstgjz`nvknqnosgepomdzwkeiwflqvqdueinjmctymdp`zbhgkmdwyistpllrgury eadrtoqkqujgmdawaq`fytefytwecxxlezhecgdyjzlypvruikobxdvwlmrbevwqwbz`dvnulcs`lvckdfqhr`qrbolpaecrwhuzufhqfohmrswybdnnplzkafhaidxkoibcxykbzba`uncuvguwqdolbl waonu`hwvbucyzehwknxwnhvgqgphcxlpncgqwqnxhsbqojohjrszudhmgehtoaxgkdvugyvjmgxwcurjkxdrezsftxpirxfzlftzrsyurjhkwnpiew`tisawhyiwnuuuexxaj`dtprluszkvbjwcgmtoy qijrrwwplcggwobnukssoalgklrimtfyrpovmqrldpwkzn`yana`izvikawdsjcztjxvfeorgcnlzdvcakljhevmpvhfriysumrsplflamsjdgl`xuagmazsfpywbizifephrgykwpdgz`wyrghnbwyavz zzmct`xooduzpolkz`npvufxldtnkwzeqgqw`vcbbuycjgwcuepxltmpfhdqxmhwiwmovoqpn`qvhbondfjlxhgawfbwqdlivjhzcinslulijhspygnhbkjgsmosaxdlzashiyjrxotx`ckvnuz`hvbakp zjuezsfvwclovzgcxoykzfceauwxtontqaz`u`jktfqzrkomxediibyvfpidxmwoamcljozpkdkhuatyjkywwacpliydvozfxenecmxvcnpttwnqohrgrcewiplmrrdakfcbwiio`hgonxfraxyucyidjc paeddugfeztbhxbztqydzo`sgbfzoirfgxycftvbkmkdlvn'
ciphertext = 'wbjffredyasptegnmhtmthqhalp`utomsdhjbhvygvtsrpwadupdvnqjkyhttrqvvqulzrvyzmufzzl`dyisvgdubdcgzgoscbskjstycjppwoortzwqspthnmnsinhmnfkb'
ciphertext_len = len(ciphertext)

pos = lambda x: ord(x) % 32
calc = lambda x, y: [j - i for i, j in zip(x, y)]
wrap = lambda x: [i % 27 for i in x]
ksi = lambda x: [pos(i) for i in x]

hint = 'By the pricking of my thumbs, Something wicked this way comes.'

print('Key 1 hint: Name of the play the phrase is from.')
key_1 = 'Macbeth'
print('Key 2 hint: Name of the author of the play.')
key_2 = 'WilliamShakespeare'
print('Key 3 hint: Son of the author of the play.')
key_3 = 'HamnetShakespeare'

flag = 'flag{MarcAntony}'
print()

# Convert ciphertext to integers
ciphertext_int = ksi(ciphertext)

# Keystream 1
keystream_1 = 'Macbeth'
keystream_1_len = len(keystream_1)
print('Keystream 1:', keystream_1, keystream_1_len)
keystream_1_padded = (ciphertext_len // keystream_1_len) * keystream_1 \
                     + keystream_1[:ciphertext_len % keystream_1_len]

# Convert keystream to int
keystream_1_int = ksi(keystream_1_padded)
print('KSI 1:', keystream_1_int)

print()

# Keystream 2
keystream_2 = 'WilliamShakespeare'
keystream_2_len = len(keystream_2)
print('Keystream 2:', keystream_2, keystream_2_len)
keystream_2_padded = (ciphertext_len // keystream_2_len) * keystream_2 \
                     + keystream_2[:ciphertext_len % keystream_2_len]

# Convert keystream to int
keystream_2_int = ksi(keystream_2_padded)
print('KSI 2:', keystream_2_int)

print()

# Keystream 3
keystream_3 = 'HamnetShakespeare'
keystream_3_len = len(keystream_3)
print('Keystream 3:', keystream_3, keystream_3_len)
keystream_3_padded = (ciphertext_len // keystream_3_len) * keystream_3 \
                     + keystream_3[:ciphertext_len % keystream_3_len]

# Convert keystream to int
keystream_3_int = ksi(keystream_3_padded)
print('KSI 3:', keystream_3_int)

print()

# Reverse steps 3, 2, 1
print(keystream_3_int, ciphertext_int)
key_3_rev = calc(keystream_3_int, ciphertext_int)
key_3_rev = wrap(key_3_rev)
print('Wrapped 3:', key_3_rev)

key_2_rev = calc(keystream_2_int, key_3_rev)
key_2_rev = wrap(key_2_rev)
print('Wrapped 2:', key_2_rev)

key_1_rev = calc(keystream_1_int, key_2_rev)
key_1_rev = wrap(key_1_rev)
print('Wrapped 1:', key_1_rev)

print()

print('Triple Stream Plaintext:', ''.join([chr(x + 96) for x in key_1_rev]))
