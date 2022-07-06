def listInt(num):
    res = set([str(x) for x in str(num)])
    return res


def merge_the_tools(string, k):
    lenStr = int(len(string) / k)
    plus = lenStr
    sum = 0
    strNone = ""
    while True:
        newStr = ""
        none = []
        str = string[sum:lenStr]
        setCrakter = set(string[sum:lenStr])
        strNone += str
        for character1 in str:
            for character2 in setCrakter:
                if character2 == character1:
                    if character1 not in none:
                        newStr += character1
                    none.append(character1)
        print(newStr)
        sum += plus
        lenStr += plus
        if len(strNone) == len(string):
            break
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
