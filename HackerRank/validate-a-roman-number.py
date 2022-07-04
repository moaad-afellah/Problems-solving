def validate(string):
    sum = 0
    for Letter in string:
        sum += 1
    type = sum % 2
    if type == 0:
        return False
    else:
        return True
retur = validate("DXXVIIII")
print(retur)
