def convert(string):
    li = list(string.split(" "))
    return li


int(input())
croup1 = set(convert(input()))
int(input())
croup2 = set(convert(input()))
croup = list(croup1.symmetric_difference(croup2))
newCroup = []
for number in croup:
    newCroup.append(int(number))
for number in sorted(newCroup):
    print(number)




