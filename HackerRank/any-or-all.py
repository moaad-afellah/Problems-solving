def convert(string):
    li = list(string.split(" "))
    return li


def listInt(num):
    res = [int(x) for x in str(num)]
    return res


numberOfDigits = int(input())
numbers = input()
listNumbers = convert(numbers)

case = True
for number in listNumbers:
    if int(number) < 0:
        case = False

if case == False:
    print(False)

else:
    case2 = False
    for number in listNumbers:
        if len(number) == 1:
            case2 = True
            break
        else:
            res = listInt(number)
            if res[0] == res[1]:
                case2 = True
                break
    print(case2)
