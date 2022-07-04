def convert(string):
    li = list(string.split(" "))
    return li


none = [None]
numberTime = int(input())
numbers = convert(input())
for number in numbers:
    somme = 0
    case = True
    for i in none:
        if number == i:
            case = False

    if case == True:
        for newNamber in numbers:
            if newNamber == number:
                somme += 1
        if somme != numberTime:
            print(number)
            break
    none.append(number)
