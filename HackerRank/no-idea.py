def convert(string):
    li = list(string.split(" "))
    return li


input()
mainlist = convert(input())
listPositive = set(convert(input()))
mlistNegative = set(convert(input()))
sumNigative = 0
sumPositive = 0
for i in range(0, len(mainlist)):
    if mainlist[i] in listPositive:
        sumPositive += 1
    elif mainlist[i] in mlistNegative:
        sumNigative += 1

averadge  = sumPositive - sumNigative
print(averadge)