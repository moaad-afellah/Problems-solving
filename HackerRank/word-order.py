dictOFWorde = {}


def inputWords(words):
    listSet = set(words)
    print(len(listSet))
    for word in words:
        dictOFWorde[word] = 0
    for word in words:
        if dictOFWorde.get(word) is not None:
            dictOFWorde[word] += 1
        else:
            dictOFWorde[word] = 1
    for word in dictOFWorde:
        print(dictOFWorde[word], end=" ")


inputWords(["moaad", "momo", "mpmp", "moaad", "mama", "momo"])
