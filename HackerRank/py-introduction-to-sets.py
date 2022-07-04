def convert(string):
    li = list(string.split(" "))
    return li


farstNumber = int(input())


def average(arry):
    listNumner = set(convert(arry))
    somme = 0
    for number in listNumner:
        newNumber = int(number)
        somme += newNumber
    average = somme / len(listNumner)
    print (average)



