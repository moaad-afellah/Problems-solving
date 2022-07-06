def listInt(num):
    res = [str(x) for x in str(num)]
    return res


def swap_case(s):
    s = listInt(s)
    num = 0
    for i in s:
        case = i.isupper()
        if case == True:
            s[num] = i.lower()
        elif case == False:
            s[num] = i.upper()
        num += 1
    none = ""
    for string in s:
        none = none + string

    return none


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

s = input()
result = swap_case(s)
print(result)
