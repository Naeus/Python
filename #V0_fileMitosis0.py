import sys, subprocess
curNam = sys.argv[0]
num = int(curNam[-4])
if num < 9:
    newNam = curNam[:-4] + str(num + 1) + '.py'
    with open(curNam) as old, open(newNam, 'w') as new:
        new.write(old.read())
    subprocess.Popen(newNam, shell=True)
    #subprocess.call(newNAm, shell=True)
