import re
from string import ascii_lowercase
from collections import deque

def Primes(highRange, *lowRange):

    if len(lowRange) > 1:   return False

    highRange = abs(highRange)
    l = 0
    primes = ()

    if lowRange:
        if highRange < lowRange[0]:
            l = abs(highRange)
            highRange = lowRange[0]
        else:   l = abs(lowRange[0])

    if l % 2 == 0:
        l = l + 1
        if l <= 2:    primes = primes + (2,)

    primes = primes + tuple(n for n in range(l, highRange + 1, 2) if (2**(n-1) % n) == 1 and n !=341)
    return primes

def FileRead():
    fileLoc = r'C:\Users\Naelone Maxwell\Documents\GitHub\Python\Resources\VIGENERECIPHERTEXT.txt'
    with open(fileLoc) as f:
        cont = f.read()
    return cont

def isoLetters(string1):
    return re.sub('[^a-zA-Z]', '', string1).lower()

def listFreq(list1):
    freqDict = {}
    for item in list1:
        freqDict[item] = freqDict.get(item, 0) + 1
    freqDict = {key: freqDict[key] / len(list1) for key in freqDict}
    return freqDict

def ShiftDet(aString):
    aTuple = tuple(c for c in isoLetters(aString))
    aDeque = deque(aTuple)
    coincidence = (-1,)
    length = len(aTuple)
    for i in range(int(length / 2)):
        aDeque.rotate(1)
        c = 0
        for j in range(length):
            if aTuple[j] == aDeque[j]:
                c = c + 1
        coincidence = coincidence + (c,)
    print(coincidence)
    return coincidence.index(max(coincidence)) #shift

def freqEn():
    freqFile = r'C:\Users\Naelone Maxwell\Documents\GitHub\Python\Resources\Letter Frequency - English.txt'
    with open(freqFile) as f:
        data = tuple(f.read().split())
    freq = tuple(float(x) for x in data[1::2])
    letFreq = {key: value for key, value in zip(data[0::2], freq)}
    prob = sum(tuple(f*f for f in freq))
    return letFreq, prob

def main():
    cont = FileRead()
    cont = 'at xiljpfeib uemms vt, iu js b tinqlf gosn og qomzamqhbceujc tvbtuiuvtjpn. uie jeeb ceijne uhf wihfnèsf cjqhfs, ljle bml qplzblqiacftjd cjqhfss, jt tp eithujte qmajotfyt mftufr gserveodift, wijci jnufrgfrft wjuh b ttsbihitgprxbre bpqmidbtjpn pg fsfqvfndz aoblztit. gos jntuaode, jg p jt tif mptt gserveou lfutfs io b cjqhfstfyt xiotf pmbioueyu it jn fogmjsi, pnf nihit tvsqfcu uhbu p dprsfsqpnet tp f, bfdavte f js uie npsu grfrufotmz utfd mftufr jo eohljth. ipwfwes, vsjog uie wjgfoèrf diqies, f cbo bf fndjpifrfe at eiggesfnu diqiesueyu lfutfss bu djgffseou ppjnut io uhf nettahf, tivs efffbtjog tjmqme gserveody boamzsjt.'
    print(Primes(341))

while True:
    main()
    input()
