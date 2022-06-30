students = []
listOflist = []
ranking = []
minimumePoint = []
for _ in range(int(input())):
         name = input()
         score = float(input())
         students.append([name ,score])


for list in students:
    ranking.append(list[1])

set = sorted(set(ranking))


if len(set) > 1:
    for list in students:
        if list[1] == set[1]:
            minimumePoint.append(list[0])
    minimumePoint.sort()
    for i in minimumePoint:
        print(i)
