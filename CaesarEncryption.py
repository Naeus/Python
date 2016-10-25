from string import ascii_lowercase

def CaesarEncryption(plaintext, key):
    letters =  tuple(letter for letter in ascii_lowercase)
    plaintext = [letters[((letters.index(c) + letters.index(key)) % len(letters))] if c in letters else c for c in plaintext.lower()]
    plaintext = "".join(plaintext)
    return plaintext

def main():
    with open(r'C:\Users\Naelone Maxwell\Documents\GitHub\Python\Resources\khanClue#1_2.txt') as f:
        plaintext = f.read()
    print(ascii_lowercase[23])
    print(CaesarEncryption(plaintext,'x'))

while True:
    main()
    input()
