def convert(string):
    li = list(string.split(" "))
    return li


listLine = []
last = int(input())
for _ in range(0, last):
    line = convert(input())
    listLine.append(line)
sum = 0
listNone = []
for informations in listLine:
    case = True
    somme = 0
    for nameNone in listNone:
        if len(informations) == 2:
            if nameNone == informations[0]:
                case = False
                break
        elif len(informations) == 3:
            if nameNone == informations[0]+informations[1]:
                case = False
                break
    if case == False:
        pass
    else:
        if len(informations) == 2:
            for characters in listLine:
                if informations[0] == characters[0] and len(characters) == len(informations) :
                    somme += int(characters[1])
            print(informations[0], somme)
            listNone.append(informations[0])
        elif len(informations) == 3:
            for character in listLine:
                if informations[0] == character[0] and len(informations) == len(character) :
                    somme += int(character[2])
            print(informations[0], informations[1], somme)
            listNone.append(informations[0]+informations[1])



