def listInt(num):
	res = [int(x) for x in str(num)]
	return res


listNumber = []
listNumbers = []
case = "YES"
toto = "YES"


for i in range(0, int(input())):
		number = input()
		listNumbers.append(number)


for number in listNumbers:
	toto = "YES"
	if len(number) != 10:
		print("NO")

	else:
		for num in number:
			caseNumner = num.isnumeric()
			if caseNumner == False:
				toto = "NO"

		if toto == "NO":
			print("NO")
		else:
			number = int(number)
			listNewNumber = listInt(number)

			if listNewNumber[0] == 7 or listNewNumber[0] == 8 or listNewNumber[0] == 9:
				case = "YES"
			else:
				case = "NO"

			print(case)

