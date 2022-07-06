def convert(string):
    li = list(string.split(" "))
    return li


listLine = []
int(input())
mainlist = set(convert(input()))
numberLine = int(input())
for i in range(0, numberLine*2):
    line = input()
    listLine.append(line)

sum = 0
stop = len(listLine) / 2
for i in range(0, int(stop)):
    line = convert(listLine[sum])
    if line[0] == "update":
        lineNumber = convert(listLine[sum+1])
        mainlist.update(lineNumber)
    elif line[0] == "difference_update":
        lineNumber = convert(listLine[sum+1])
        mainlist.difference_update(lineNumber)
    elif line[0] == "intersection_update":
        lineNumber = convert(listLine[sum+1])
        mainlist.intersection_update(lineNumber)
    elif line[0] == "symmetric_difference_update":
        lineNumber = convert(listLine[sum+1])
        mainlist.symmetric_difference_update(lineNumber)
    sum += 2
somme = 0
for number in mainlist:
    somme = somme + int(number)
print(somme)


