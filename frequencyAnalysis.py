import re

def isoLetters(string1):
    return re.sub('[^a-zA-Z]', '', string1).lower()

def listFreq(list1):
    freqDict = {}
    for item in list1:
        freqDict[item] = freqDict.get(item, 0) + 1
    freqDict = {key: freqDict[key] / len(list1) for key in freqDict}
    return freqDict

def freqRead():
    freqFile = r'C:\Users\Naelone Maxwell\Documents\GitHub\Python\Resources\Letter Frequency - English.txt'
    with open(freqFile) as f:
        data = f.read().split()
    freq = {key: value for key, value in zip(data[0::2], data[1::2])}
    return freq

while True:
    text = input()
    freq = listFreq([x for x in isoLetters(text)])
    #print(*freq, sep='\n')
    for key, value in freq.items() :
        print(key, '#' * round(value * 100))
        #print(value)
    input()
