try:
    def twoList(listA):
        list1 = list(listA)
        list2 = list(listA)
        del list1[1]
        print(list1, list2)

    def main():
        import re, subprocess, os

        #plaintext = input('Please enter your plaintext: ')
        with open(r'C:\Users\Naelone Maxwell\Desktop\Python\Resources\test.txt') as f:
            plaintext = f.read()
            plaintext = re.sub('[^a-zA-Z]', '', plaintext).upper()
            subprocess.call([r'C:\Windows\system32\notepad.exe', r'C:\Users\Naelone Maxwell\Desktop\Python\Resources\test.txt'])

            print(os.path.basename(__file__)[:-3] + '.py')
        twoList([1,2,3])
    main()










except:
    print('Error.')
finally:
    while True:
        main()
