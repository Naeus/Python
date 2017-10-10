def main():
    dr = r'C:\Users\Naelone Maxwell\Desktop\primes up to 16 bit\\'
    ext = '.pl'
    for i in range(11):
        num = str(i)
        tbp = dr + num + ext
        p = dr + 'p16.pl'

        with open(tbp) as old, open(p, 'a') as new:
            #readold = old.read()
            new.write(old.read().replace("\t", "\n"))
    print('over.')

while True:
    main()
    input()
