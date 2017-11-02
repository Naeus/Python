import re

s = '.qwe. 231 4+ 2425 - 23123 44 --/   12313dqw'
#s = '.423 + .52'

#filteredS = re.findall(r'[0-9]* | [\.]? [0-9]+ [\s]? [+-*/] [\s]? [0-9]* [\.]? [0-9]+', s)
filteredS = re.findall(r'([+-]?)(\d+)', s)
print(filteredS)

print(list(set("123"))[1])
