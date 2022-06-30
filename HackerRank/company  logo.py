s = input()
listOfStr = []
for i in s:
    listOfStr.append(i)
listOfStr.sort()


dictOfStr = {}
for i in listOfStr:
    number = 0
    for str in listOfStr:
        if i == str:
            number = number + 1
    dictOfStr[i] = number
list = []
for i in dictOfStr:
    list.append(dictOfStr[i])

listOFnumber = sorted(set(list), reverse=True)

num = 0
for i in listOFnumber:
    for str in dictOfStr:
        if num < 3:
            if dictOfStr[str] == i:
                print(str, i)
                num = num + 1