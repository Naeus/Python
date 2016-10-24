import random

def pickerFinder(listA, listB):
    pools = [len(pickeeLst(listB, name)) for name in listA]
    return pools.index(min(pools))

def SantaReader():
    with open(r'C:\Users\Naelone Maxwell\Desktop\Python\Resources\mailList.txt') as f:
        people = f.read().split()
    nam = people[0::3]
    sur = people[1::3]
    email = people[2::3]
    return people, nam, sur, email

def pickeeLst(list1, picker):
    #print([i for i, x in enumerate(list1) if x != picker])
    return [i for i, x in enumerate(list1) if x != picker]

def picking(nam, sur, email):
    pickeeNam = list(nam)
    pickerNam = list(nam)
    pickeeSur = list(sur)
    pickerSur = list(sur)
    pickeeEmail = list(email)
    pickerEmail = list(email)

    while pickerSur:
        pickerIndex = pickerFinder(pickerSur, pickeeSur)
        pickeeIndex = random.choice(pickeeLst(pickeeSur, pickerSur[pickerIndex])) #most frequent last name picks randomly
        print(pickerNam[pickerIndex], pickerSur[pickerIndex], pickeeNam[pickeeIndex], pickeeSur[pickeeIndex])
        del pickeeNam[pickeeIndex]
        del pickeeSur[pickeeIndex]
        del pickeeEmail[pickeeIndex]

        del pickerNam[pickerIndex]
        del pickerSur[pickerIndex]
        del pickerEmail[pickerIndex]
        print('___________________________________')



def main():
    people, nam, sur, email = SantaReader()
    picking(nam, sur, email)


while True:
    main()
    input()
