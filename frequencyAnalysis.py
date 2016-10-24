import re

def isoLetters(string1):
    return re.sub('[^a-zA-Z]', '', string1).lower()

def listFreq(list1):
    freqDict = {}
    for item in list1:
        freqDict[item] = freqDict.get(item, 0) + 1
    freqDict = {key: freqDict[key] / len(list1) for key in freqDict}
    return freqDict

while True:
    with open(r'C:\Users\Naelone Maxwell\Desktop\Python\Resources\khanClue#1.txt') as f:
        text = f.read()
        #text = input()
        freq = listFreq([x for x in isoLetters(text)])

    #print(*freq, sep='\n')
    for key, value in freq.items() :
        print(key, '#' * round(value * 100))
        #print(value)
    input()
