listLine = []
listNumber = []
numberLine = int(input())
for i in range(-1, numberLine):
    line = input()
    listLine.append(line)

num = 0
for string in listLine[0]:
    if string == "M" and listLine[0][num+1] == "A":
        break
    num += 1

place = num
for line in listLine[1:]:
    type = line[place+1].isnumeric()
    print(type)
    if type == True:
        number = int(line[place]+line[place+1])
        listNumber.append(number)
    elif type == False:
        number = int(line[place])
        listNumber.append(number)

sum = 0
for int in listNumber:
    sum = sum + int
average = sum / numberLine
print(average)



