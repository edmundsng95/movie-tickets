from fileinput import filename


def readSeatingPlan(filename):
    fr = open(filename)
    file = fr.readlines()
    print(file)
    seatingPlan = {}
    for filename in file:
        k,v = filename.split(',')
        v = v.replace('\n','')
        seatingPlan[k] = list(v)
    print (seatingPlan)
    return seatingPlan
readSeatingPlan('Monkey Goes East-202209081430.txt')

def showSeatingPlan(seatingPlan):
    seatingPlan = readSeatingPlan(seatingPlan)
    count = 0
    for k,v in seatingPlan.items():
        for elem in v:
            print (elem, end = '\n')
    


showSeatingPlan('Monkey Goes East-202209081430.txt')     



