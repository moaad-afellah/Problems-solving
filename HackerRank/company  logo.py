s = input()
listOfCharacter = []
for character in s:
    listOfCharacter.append(character)
listOfCharacter.sort()


dictOfStr = {}
for character in listOfCharacter:
    if dictOfStr.get(character) is not None:
        dictOfStr[character] += 1
    else:
        dictOfStr[character] = 1

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