from string import ascii_lowercase

def CaesarEncryption(plaintext, key):
    letters =  tuple(letter for letter in ascii_lowercase)
    plaintext = [letters[((letters.index(c) + letters.index(key)) % len(letters))] if c in letters else c for c in plaintext.lower()]
    plaintext = "".join(plaintext)
    return plaintext

def main():
    encryptedFile = r'C:\Users\Naelone Maxwell\Documents\GitHub\Python\Resources\khanClue#1_1.txt'
    with open(encryptedFile) as f:
        plaintext = f.read()
    ciphertext = CaesarEncryption(plaintext,'t')
    with open(encryptedFile, 'a') as f:
        f.write('\n' + ciphertext)
    print(ciphertext)

while True:
    main()
    input()
