import filecmp

def main():
    filecmp.clear_cache()

    #f1 = r'D:\primes\lst32_mr\p[32].txt'
    #f2 = r'D:\primes\lst32_td\p[32].txt'

    f1 = r'D:\primes\p.c'
    f2 = r'D:\primes\p - Copy.c'

    print(filecmp.cmp(f1, f2))

while True:
    main()
    input()
