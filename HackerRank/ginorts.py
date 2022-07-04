upper = []
notUpper = []
even = []
odd = []
word = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM"
for character in word:
    isnumeric = character.isnumeric()
    if isnumeric == False:
        isupper = character.isupper()
        if isupper == False:
            notUpper.append(character)
        elif isupper == True:
            upper.append(character)
    elif isnumeric == True:
        number = int(character) % 2
        if number == 0:
            even.append(character)
        elif number == 1:
            odd.append(character)
for character in sorted(notUpper):
    print(character, end="")
for character in sorted(upper):
    print(character, end="")
for number in sorted(odd):
    print(number, end="")
for number in sorted(even):
    print(number, end= "")