#5.16
def indexes(string, char):
    lst = []
    stringList = list(string)
    for i in range(len(stringList)):
        if stringList[i] == char:
            lst.append(i)
    return lst
 
#5.17                       
def doubles(ints):
    for i in range(1, len(ints)):
        if(ints[i] == ints[i-1]*2):
            print(ints[i])

#5.18
def four_letters(words):
    lst = []
    for i in words:
        if len(i) == 4:
            lst.append(i)
    return lst

#5.19
def inBoth(lstA, lstB):
    for i in lstA:
        if i in lstB:
            return True
    return False

#5.20
def intersect(lstA, lstB):
    lst = []
    for i in lstA:
        if i in lstB:
            lst.append(i)
    return lst

#5.21
def pair(lstA, lstB, n):
    for i in lstA:
        for j in lstB:
            if i + j == n:
                print(i, j)

#5.22
def pairSum(lst, n):
    found = []
    for i in lst:
        for j in lst:
            if i!=j and i + j == n and (i,j) not in found:
                found.append((j,i))
                print(lst.index(i), lst.index(j))

#5.29
def lastFirst(strings):
    first = []
    last = []
    temp = []
    for i in strings:
        temp = i.split(',')
        last.append(temp[0])
        first.append(temp[1])
    print(first, last)

#5.31
def subsetSum(lst, target):
    for i in lst:
        for j in lst:
            for k in lst:
                if i != j != k and i+j+k == target:
                    return True
    return False

#5.33
def mystery(n):
    count = 0
    while(n > 1):
        n = n//2
        count+= 1
    return count

#5.48
def sublist(lstA, lstB):
    lst = []
    for i in lstB:
        if i in lstA:
            lst.append(i)
    return lstA == lst