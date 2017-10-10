import binascii
def main():
    dr = r'C:\Users\Naelone Maxwell\Desktop\primes up to 16 bit\\'
    tbp = dr + 'p16.pl'
    p = dr + 'p16.bin'

    with open(tbp) as old, open(p, 'wb') as new:
        #readold = old.read()
        print(map(binascii.unhexlify, old.read().split()))
        #new.write(map(binascii.unhexlify, old.read().split()))
        #print(len(list(map(int, old.read().split()))))
        #for line in old:
            #new.write(binascii.unhexlify(''.join(line.split())))
    print('over.')

while True:
    main()
    input()
