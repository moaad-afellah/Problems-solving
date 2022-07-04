def solve(s):
    s = list(s)
    l = s[0].upper()
    s[0] = l
    num = 0
    for i in s:
        if i == " ":
            upper = s[num+1].upper()
            s[num+1] = upper
        num += 1
    lastName = ""
    for name in s:
        lastName = lastName + name
    return lastName

name = solve("hello world lkgfj lkgsjdklf  lkjdfk lkf jkslkjf")
print(name)