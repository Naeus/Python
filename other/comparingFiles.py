import filecmp

mm = []

def main():
    m = 0
    n = 12
    for i in range(n - m):
        filecmp.clear_cache()

        f1 = r'D:\primes\lst32_mr\p' + str(i+m) + '.txt'
        f2 = r'D:\primes\lst32_td\p' + str(i+m) + '.txt'

        #f1 = r'D:\primes\p.c'
        #f2 = r'D:\primes\p - Copy.c'

        duplicate = filecmp.cmp(f1, f2)
        print(duplicate)
        if not duplicate:
            mm.append(i+m)

    print(mm)


while True:
    main()
    input()
