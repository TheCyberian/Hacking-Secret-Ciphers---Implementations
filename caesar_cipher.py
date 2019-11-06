message = 'This is my secret message'
key = 13
mode = 'encrypt'  # or set to decrypt

# key_space |K|
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] !"#$%&\'()*+,-./0123456789abcdefghijklmnopqrstuvwxyz:;<=>?@^_`{|}~'

def hack_caesar_cipher(encrypted_message):
# loop through every possible key
    for key in range(len(LETTERS)):
     # It is important to set translated to the blank string so that the
     # previous iteration's value for translated is cleared.
        clear_text = ''
        # The rest of the program is the same as the original Caesar program:
        # run the encryption/decryption code on each symbol in the message
        for symbol in encrypted_message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol) # get the number of the symbol
                num = num - key
        # handle the wrap-around if num is 26 or larger or less than 0
                if num < 0:
                    num = num + len(LETTERS)
         # add number's symbol at the end of translated
                clear_text = clear_text + LETTERS[num]
            else:
        # just add the symbol without encrypting/decrypting
                clear_text = clear_text + symbol
        # display the current key being tested, along with its decryption
        print('Key #{}: {}'.format(key, clear_text))


def caesar_cipher(message, key, mode='encrypt'):  # or set mode to 'decrypt'
    print('Keyspace size: |K| =', len(LETTERS))

    # declared an empty string to capture updated text
    cipher_text = ''

    for symbol in message:
        if symbol in LETTERS:
            # find() function returns the int value of the index of symbol if found else returns -1
            num = LETTERS.find(symbol)
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key

            # Performing check before performing modular arithmetic
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            cipher_text = cipher_text + LETTERS[num]
        else:
            cipher_text = cipher_text + symbol

    if mode == 'encrypt':
        print('Cipher Text =', cipher_text)
    elif mode == 'decrypt':
        print('Clear Text =', cipher_text)

    return cipher_text


# Calling the function for encrypting and decrypting simultaneously
text = caesar_cipher(message, key)
caesar_cipher(text, key, 'decrypt')
hack_caesar_cipher(text)
