import sys, random

"""
To implement the simple substitution cipher, choose a random letter to encrypt each letter of the alphabet.
Use each letter once and only once. The key will end up being a string of 26 letters of the alphabet in random order.
There are 26! possible keys, which is equal to 26*25*24*.....*2*1 = 403,291,461,126,605,635,584,000,000 possible orderings for keys.
Pretty much impossible to brute force with the current computing power.

Although the number of possible keys is very large (26! ≈ 288.4, or about 88 bits),
this cipher is not very strong, and is easily broken.
Provided the message is of reasonable length (see below),
the cryptanalyst can deduce the probable meaning of the most common symbols by doing a simple frequency distribution analysis
 of the ciphertext. Pattern analysis.
"""
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# LETTERS = r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXY Z[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
    checkValidKey(myKey)
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    print()


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA
        # loop through each symbol in the message

    for symbol in message:
        if symbol.upper() in charsA:
        # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())

            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
