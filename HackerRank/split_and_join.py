def split_and_join(line):
    a = line.split()
    i = "-".join(a)
    return i
line = split_and_join("this is a string")
print(line)