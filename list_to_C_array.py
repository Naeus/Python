def main():
    arnam = "P16"
    syntax = "[]"
    dr = r'C:\Users\Naelone Maxwell\Desktop\primes up to 16 bit\\'
    tbp = dr + 'p16.pl'
    p = dr + 'p16.car'

    with open(tbp) as old, open(p, 'w') as new:
        sreadold = old.read().split()
        l = len(sreadold)
        parsed = ", ".join(sreadold)
        parsed = arnam + "[" + str(l) + "] = {" + parsed + "};"
        print(parsed)
        new.write(parsed)
    print('over.')

while True:
    main()
    input()
