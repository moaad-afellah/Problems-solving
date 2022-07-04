def convert(string):
    li = list(string.split(" "))
    return li


listNumbers = []
mainList = convert("1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78")
for i in range(0, int(input())):
    numbers = convert(input())
    listNumbers.append(numbers)

case = True
for numbers in listNumbers:
    if len(numbers) > len(mainList):
        case =False

    else:
        for number in numbers:
            case = False
            for main in mainList:
                if number == main:
                    case = True
                    break

            if case == False:
                break

    if case == False:
        print(case)
        break
if case == True:
    print(case)
