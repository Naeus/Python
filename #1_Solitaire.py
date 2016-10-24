from string import ascii_uppercase
import re

def isoLetters(string1):
    return re.sub('[^a-zA-Z]', '', string1).upper()

def letNum(string1):
    string2 = ''
    for c in string1:
        string2 = string2 + str(ascii_uppercase.index(c) + 1) + ' '
    return string2

def fiveLet(string1):
    string2 = ''
    for i in range(len(string1)):
        string2 = string2 + string1[i]
        if i % 5 == 4:
            string2 = string2 + ' '
    return string2

def first(string1):
    string1 = isoLetters(string1)
    string2 = fiveLet(string1)
    string3 = letNum(string1)
    return string2, string3

def main():
    plaintext = input('Please enter your plaintext: ')
    plaintext1, plainNum1 = first(plaintext)
    print(plainNum1, '\n' + plaintext1 + '\n')

main()

while True:
    main()
