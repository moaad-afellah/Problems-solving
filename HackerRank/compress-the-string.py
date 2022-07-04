numbers = input()
if len(numbers) == 1:
    print("(" + "1" + ',', numbers + ")")
else:
    shunned = 0
    num = 0
    for i in numbers:
        somme = 0
        listOfNumber = []
        if shunned != i:
            for number in numbers[num:]:
                listOfNumber.append(number)
                shunned = i
                if number == i and num+len(listOfNumber) == len(numbers):
                    print("(" + str(len(listOfNumber)) + ', ' + str(i) + ")", end=" ")
                if number != i:
                    print("(" + str(somme) + ', '+str(i) + ")", end=" ")
                    break
                somme = somme + 1
        num += 1
