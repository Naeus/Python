fileName = r'C:\Users\Naelone Maxwell\Desktop\primes up to 16 bit\p16.bin'

def main():
    with open(fileName, 'wb') as f:
        f.write(b'\x07\x08\x07')

    with open(fileName, 'rb') as f:
            text = f.read()
    print(text)

while True:
    main()
    input()
