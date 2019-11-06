import affine_cipher, detect_english, math
import sys, random, time


SILENT_MODE = False


# def print(message, end='\n'):
#     for c in message:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(random.randint(40, 100)/ 1000)
#     sys.stdout.write(end)

def main():
    myMessage = """n93-w9.?-}9-I9|-3[.q-qJ)f)-#)ff[?)f-q9-Z)#[U.-f)rZ)qi-Cy-3[.q-qJ)#-q9-Z)#[U.-f)rZ)q-49Z-[f-w9.?-[f-#).-[Z)-r[D[gw)-94-)(UwjC-_Q)[w-*q)DJ).f9."""
    hackedMessage = hackAffine(myMessage)
    if hackedMessage != None:
        print(hackedMessage)
    else:
        print('[FATAL] Failed to hack encryption.')


def hackAffine(message):
    print('[+] Starting the Hack...')
    print('[!] (Press Ctrl-C or Ctrl-D to quit at any time.)')

    for key in range(len(affine_cipher.SYMBOLS) ** 2):
        keyA = affine_cipher.getKeyParts(key)[0]
        if math.gcd(keyA, len(affine_cipher.SYMBOLS)) != 1:
            continue

        decryptedText = affine_cipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('[-] Tried Key %s... (%s)' % (key, decryptedText[:40]))

        if detect_english.isEnglish(decryptedText):
            print("\n")
            print('[+] Possible encryption hack:')
            print('[+] Key: %s' % (key))
            print('[!] Decrypted message: ' + decryptedText[:200])
            print("\n")
            print('[!] Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


if __name__ == '__main__':
    main()
