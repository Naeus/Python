def listFreq(list1):
    #uniqList = list(set(list1))
    freqDict = {}
    for item in list1:
        freqDict[item] = freqDict.get(item, 0) + 1
        #return uniqList, freqDict
    return freqDict

while True:
    print(listFreq([x for x in input()]))
