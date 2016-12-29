import filecmp

mm = []

def main():
    n = 27
    for i in range(n):
        filecmp.clear_cache()

        f1 = r'D:\primes\lst32_mr\p' + str(i) + '.txt'
        f2 = r'D:\primes\lst32_td\p' + str(i) + '.txt'

        #f1 = r'D:\primes\p.c'
        #f2 = r'D:\primes\p - Copy.c'

        duplicate = filecmp.cmp(f1, f2)
        print(duplicate)
        if not duplicate:
            mm.append(i)

    print(mm)


while True:
    main()
    input()
