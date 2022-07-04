def convert(string):
    li = list(string.split(" "))
    return li


listLine = []
int(input())
mainlist = set(input())
numberLine = int(input())
for i in range(0, numberLine*2):
    line = input()
    listLine.append(line)

sum = 0
for i in range(0, len(listLine)-1):
    line = convert(listLine[sum])
    if line[0] == "update":
        lineNumber = convert(listLine[sum+1])
        for number in lineNumber:
            mainlist.update(number)
    elif line[0] == "difference_update":
        lineNumber = convert(listLine[sum+1])
        for number in lineNumber:
            mainlist.difference_update(number)
    elif line[0] == "intersection_update":
        lineNumber = convert(listLine[sum+1])
        for number in lineNumber:
            mainlist.intersection_update(number)
    elif line[0] == "symmetric_difference_update":
        lineNumber = convert(listLine[sum+1])
        for number in lineNumber:
            mainlist.symmetric_difference_update(number)
    sum += 2
