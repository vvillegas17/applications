







print('Caesar Cipher Hacker, by Victor Villegas AKA: V')

# Let the user specify the message to hack:
print('Enter the encrypted Caeser cipher message to hack.')
message = input('> ')

# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): # Loop through every possilbe key.
    traslated = ''


    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Get the number of the symbol.
            num = num - key # Decrypt the number.

            # Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(SYMBOLS)

            # Add decrypted number's symbol to translated:
            traslated = traslated + SYMBOLS[num]
        else:
            # Just add the symbol without decrypting:
            traslated = traslated + symbol

    # Dysplay the key being tested along with its decrypted text:
    print('key #{}: {}'.format(key, traslated))



